import pymysql, os, time, app_utilities
from dotenv import load_dotenv
from tabulate import tabulate


def connect_to_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    return pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    
def disconnect_from_database():
    connection.close()


def read_from_database(query):
    list_from_database = []
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for row in rows:
        forming_dict = {}
        j = 0
        for x in row:
            forming_dict[field_names[j]] = x
            j += 1
        list_from_database.append(forming_dict)
    cursor.close()
    connection.commit()
    return list_from_database 


def print_table(list, table):
    if table == 'products':
        header = ['Product ID', 'Product Name', 'Price']
    elif table == 'couriers':
        header = ['Courier ID', 'Courier Name', 'Phone Number']
    elif table == 'orders':
        header = ['Order ID', 'Customer Name', 'Phone Number', 'Address', 'Status', 'Courier ID']
        
    rows = [x.values() for x in list]
    print(tabulate(rows, header, tablefmt = 'simple'))    


def print_table_function(table, query):
    list = read_from_database(query)
    print_table(list, table)

# ---------------------------------------------------------------------------
    
def execute_sql_select(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    return cursor.fetchall()
    
    
def execute_sql_update(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    connection.commit()


def choose_order_items():
    existing_ids = [id[0] for id in execute_sql_select('SELECT product_id from products')]
    basket = []
    print('')
    print_table_function('products', f'SELECT * FROM products')
    print('')
    while True:
        id = input('Please choose a product ID you wish to add. When your order is complete enter 0: ... ')
        try:
            id = int(id)
            if id == 0:
                break
            elif id not in existing_ids:
                print('ID not recognised. Please enter an existing ID.')
            elif id in existing_ids:
                basket.append(str(id))
        except ValueError:
            print('ID not recognised. Please enter an ID number.')
    return basket
    
    
def update_basket():
    cursor = connection.cursor()
    print_table_function('orders', f'SELECT * FROM orders')
    print('')
    order_id = choose_an_existing_id('orders')
    if order_id == '0':
        return
    customer_order = read_from_database(f'SELECT p.product_id, p.product_name, p.product_price FROM customer_orders c JOIN products p ON c.product_id = p.product_id WHERE c.order_id = {order_id}')
    print_order_table(customer_order) 
    print(customer_order)
    execute_sql_update(f'DELETE FROM customer_orders WHERE order_id = {order_id}')
    print('\nPlease reselect you order, including any changes.')
    basket = choose_order_items()
    print(basket)
    for product_id in basket:
        execute_sql_update(f'INSERT INTO customer_orders (order_id, product_id) VALUES ({order_id}, {product_id})')
    print('ITEMS UPDATED')
    cursor.close()
    connection.commit()
    
    
def add_to_basket():
    cursor = connection.cursor()
    order_id = execute_sql_select('SELECT MAX(order_id) FROM orders')[0][0]
    basket = choose_order_items()
    for product_id in basket:
        execute_sql_update(f'INSERT INTO customer_orders (order_id, product_id) VALUES ({order_id}, {product_id})')
    cursor.close()
    connection.commit()


def remove_database_function(table):
    id_name = get_column_names(f'SELECT * FROM {table}')[0]
    print_table_function(table, f'SELECT * FROM {table}')
    print('')
    id = choose_an_existing_id(table)
    if id == '0':
        return
    try:
        execute_sql_update(f'DELETE FROM {table} WHERE {id_name} = {id}')
        if table == 'orders':
            execute_sql_update(f'DELETE FROM customer_orders WHERE order_id = {id}')
        print('\nThe item has been successfully removed.')
    except Exception:
        print('\nCannot delete something that is already in an existing order. Returning to previous screen.')
        time.sleep(2.5)
    
    
def update_order_status():
    print_table_function('orders', f'SELECT * FROM orders')
    print('')
    order_status = ['Preparing', 'Cancelled', 'Out for delivery', 'Delivered']
    print('Press 0 to cancel operation.')
    id = choose_an_existing_id('orders')
    if id == '0':
        return
    print('')
    print(order_status)
    while True:
        status_choice = input('\nWhat is the status being updated to?: ... ').capitalize()
        if status_choice in order_status:
            execute_sql_update(f'UPDATE orders SET status = "{status_choice}" WHERE order_id = {id}')
            break
        else:
            print('That is not a valid order status.')
    print('The item has been successfully updated.')
    

def get_column_names(query):
    cursor = connection.cursor()
    cursor.execute(query)
    column_names = column_names = [i[0] for i in cursor.description]
    cursor.close()
    return column_names


def columns_and_values(column, value, column_names, string_of_values, string_of_columns):   
    if column == column_names[-1]:
        string_of_values += '"' + value + '"'
        string_of_columns += column
    else:
        string_of_values += '"' + value + '"' + ', '
        string_of_columns += column + ', '
    return string_of_columns, string_of_values


def existing_products():
    existing_products = [product[0] for product in execute_sql_select(f'SELECT product_name FROM products')]
    while True:    
        id = input(f'What would you like to add as the product name? (Enter 0 to cancel): ... ').capitalize()
        if id == '0' or id not in existing_products:
            return id
        elif id in existing_products:
            print('This product already exists. Please enter a new product.')
        
        
def add_to_database_function(table):
    print_table_function(table, f'SELECT * FROM {table}')
    print('')
    string_of_columns = ''
    string_of_values = ''
    column_names = get_column_names(f'SELECT * FROM {table}')[1:]
    for column in column_names:
        if column == 'status':
            string_of_columns, string_of_values = columns_and_values(column, 'Preparing', column_names, string_of_values, string_of_columns)
            continue
        elif column == 'courier_id':
            print('')
            print_table_function('couriers', f'SELECT * FROM couriers')
            print('')
            new_value = choose_an_existing_id('couriers')
            if new_value == '0':
                return
            new_value = str(new_value)
            string_of_columns, string_of_values = columns_and_values(column, new_value, column_names, string_of_values, string_of_columns)
            print('')
            continue
        elif column == 'product_name':
            new_value = existing_products()
            if new_value == '0':
                return
            string_of_columns, string_of_values = columns_and_values(column, new_value, column_names, string_of_values, string_of_columns)
            continue
        new_value = input(f'What would you like to add as the {column.replace("_", " ")}? (Enter 0 to cancel): ... ').title()
        if new_value == '0':
            return
        string_of_columns, string_of_values = columns_and_values(column, new_value, column_names, string_of_values, string_of_columns)
    execute_sql_update(f'INSERT INTO {table} ({string_of_columns}) VALUES ({string_of_values})')
    if table == 'orders':
        print('')
        add_to_basket()
    print('The information has been successfully added.')    


def choose_an_existing_id(table):
    id_name = get_column_names(f'SELECT * FROM {table}')[0]
    existing_ids = [id[0] for id in execute_sql_select(f'SELECT {id_name} FROM {table}')]
    while True:
        id = input('Please select an ID (Enter 0 to cancel): ... ')
        try:
            id = int(id)
            if id == 0:
                return str(0)
            elif id in existing_ids:
                break
            else:
                print('ID not recognised. Please enter an existing ID.')
        except ValueError:
            print('ID not recognised. Please enter an ID number.')    
    return id


def update_database_function(table):
    column_names_from_database = get_column_names(f'SELECT * FROM {table}')
    id_name = column_names_from_database[0]
    column_names = column_names_from_database[1:]
    print_table_function(table, f'SELECT * FROM {table}')
    print('')
    id = choose_an_existing_id(table)
    if id == '0':
        return
    print('\nLeave blank if you do not want to update.\n')
    for column in column_names:
        if column == 'status':
            continue
        new_value = input(f'What would you like to replace the {column.replace("_", " ")} with?: ... ').title()
        if new_value == '':
            pass
        else:
            execute_sql_update(f'UPDATE {table} SET {column} = "{new_value}" WHERE {id_name} = {id}')
            

def print_order_table(list):
    header = ['Product ID', 'Product Name', 'Price']
    rows = [x.values() for x in list]
    print(tabulate(rows, header, tablefmt = 'simple'))    
    
            
connection = connect_to_database() # anything to do with connection has to come to this file
# print(read_from_database(f'SELECT p.product_id, p.product_name, p.product_price FROM customer_orders c JOIN products p ON c.product_id = p.product_id WHERE c.order_id = 1'))
# update_basket()
# disconnect_from_database()