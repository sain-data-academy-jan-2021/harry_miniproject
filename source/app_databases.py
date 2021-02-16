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


def read_from_database(table):
    list_from_database = []
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table}')
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


def print_table_function(table):
    list = read_from_database(table)
    print_table(list, table)


def show_database(columns, table): # this only reads it from the database, whereas the above works for any
    cursor = connection.cursor()
    cursor.execute(f'SELECT {columns} FROM {table}')
    rows = cursor.fetchall()
    if table == 'products':
        for row in rows:
            print(f'Product ID: {str(row[0])}, Product Name: {row[1]}, Price: {row[2]}')
    elif table == 'couriers':
        for row in rows:
            print(f'Courier ID: {str(row[0])}, Courier Name: {row[1]}, Phone Number: {row[2]}')
    cursor.close()


def has_value(table, column, value):
    cursor = connection.cursor()
    return cursor.execute(f'SELECT 1 from {table} WHERE {column} = {value} LIMIT 1').fetchone() is not None


def add_to_database_function(table):
    if table == 'products':
        columns = ['product_name', 'product_price']
    elif table == 'couriers':
        columns = ['courier_name', 'phone_number']
    elif table == 'orders':
        columns = ['customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
    print_table_function(table)
    adding_for_loop(columns, table)
    print('The item has been successfully added.')
    time.sleep(1.5)
    
    
def adding_for_loop(columns, table):
    string_of_values = ''
    string_of_columns = ''
    # print('\nPress 0 to cancel operation.') this should be in the right place
    for column in columns:
        # running = True
        # while running:
        if column == 'status':
            string_of_values += '"Preparing", '
            string_of_columns += column + ', '
            # running = False
        else:
            new_value = input(f'What would you like to add as the {column.replace("_", " ")}?: ... ').title() 
            # if new_value == '0':
            #     return
            # else:
            # if column == 'product_name' or 'phone_number' or 'customer_number':
            #     if has_value(table, column, new_value):
            #         print('that already exists')
            # else:
            if column == columns[-1]:
                string_of_values += '"' + new_value + '"'
                string_of_columns += column
                # running = False
            else:
                string_of_values += '"' + new_value + '"' + ', '
                string_of_columns += column + ', '
                # running = False
    add_to_database_operation(table, string_of_columns, string_of_values)    
    
    
def add_to_database_operation(table, columns, new_values):
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({new_values})')
    cursor.close()
    connection.commit()


def update_database_function(table):
    if table == 'products':
        columns = ['product_name', 'product_price']
    elif table == 'couriers':
        columns = ['courier_name', 'phone_number']
    elif table == 'orders':
        columns = ['customer_name', 'customer_number', 'customer_address', 'courier_id']
    print_table_function(table)    
    print('\nPress 0 to cancel operation.')
    id = input('\nWhat is the id of the item you wish to update?: ... ')
    if id == '0':
        return
    else:
        app_utilities.app_title()
        print('\nLeave blank and press enter if you do not want to update.\n')
        for column in columns:
            new_value = input(f'What would you like to replace the {column.replace("_", " ")} with?: ... ').capitalize()
            if new_value == '':
                pass
            else:
                update_database_operation(table, column, new_value, id)
                print('The item has been successfully updated.')
                time.sleep(1.5)


def update_order_status():
    print_table_function('orders')
    print('\nPress 0 to cancel operation.')
    id = input('\nWhat is the id of the item you wish to update?: ... ')
    if id == '0':
        return
    else:
        order_status = ['Preparing', 'Cancelled', 'Out for delivery', 'Delivered']
        print(order_status)
        status_choice = input('\nPick a status to change the order to: ... ').capitalize()
        if status_choice in order_status:
            update_database_operation('orders', 'status', status_choice, id)
            print('The item has been successfully updated.')
            time.sleep(1.5)
        else:
            print("The order could not be updated.")
            time.sleep(1.5)


def update_database_operation(table, column, new_value, id):
    cursor = connection.cursor()
    cursor.execute(f'UPDATE {table} SET {column} = "{new_value}" WHERE id = {id}')
    cursor.close()
    connection.commit()


def remove_database_function(table):
    print_table_function(table)
    print('\nPress 0 to cancel operation.')
    id = input('\nWhat is the id of the item you wish to update?: ... ')
    if id == '0':
        return
    else:
        app_utilities.app_title()
        remove_database_operation(table, id)
        print('The item has been successfully removed.')
        time.sleep(1.5)
        

def remove_database_operation(table, id):
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE id = {id}')
    cursor.close()
    connection.commit()
    

connection = connect_to_database() # anything to do with connection has to come to this file
