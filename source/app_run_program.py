import time, app_menu_displays, app_functions, app_databases, app_utilities


def main_menu():
    app_utilities.app_title()
    option = app_menu_displays.main_menu_display()
    if option == '1':
        product_menu()
    elif option == '2':
        courier_menu()
    elif option == '3':
        order_menu()
    elif option == '4':
        app_functions.exit_app()
    else:
        app_functions.incorrect_input()
        time.sleep(1)
        main_menu()

def product_menu():
    app_utilities.app_title()
    option = app_menu_displays.product_menu_display()
    if option == '1':
        app_utilities.app_title()
        app_databases.print_table_function('products', f'SELECT * FROM products')
        input('\nPress Enter to continue. ')
        product_menu()
    elif option == '2':
        app_utilities.app_title()
        app_databases.add_to_database_function('products')
        product_menu()
    elif option == '3':
        app_utilities.app_title()
        app_databases.update_database_function('products')
        product_menu()
    elif option == '4':
        app_utilities.app_title()
        app_databases.remove_database_function('products')
        product_menu()
    elif option == '5':
        main_menu()
    elif option == '6':
        app_functions.exit_app()
    else:
        app_functions.incorrect_input()
        time.sleep(1)
        product_menu()

def courier_menu():
    app_utilities.app_title()
    option = app_menu_displays.courier_menu_display()
    if option == '1':
        app_utilities.app_title()
        app_databases.print_table_function('couriers', f'SELECT * FROM couriers')
        input('\nPress Enter to continue. ')
        courier_menu()
    elif option == '2':
        app_utilities.app_title()
        app_databases.add_to_database_function('couriers')
        courier_menu()
    elif option == '3':
        app_utilities.app_title()
        app_databases.update_database_function('couriers')
        courier_menu()
    elif option == '4':
        app_utilities.app_title()
        app_databases.remove_database_function('couriers')
        courier_menu()
    elif option == '5':
        main_menu()
    elif option == '6':
        app_functions.exit_app()
    else:
        app_functions.incorrect_input()
        time.sleep(1)
        product_menu()
        
def order_menu():
    app_utilities.app_title()
    option = app_menu_displays.order_menu_display()
    if option == '1':
        app_utilities.app_title()
        app_databases.print_table_function('orders', f'SELECT * FROM orders')
        print('\nTo see the products ordered for a customer.\n')
        id = app_databases.choose_an_existing_id('orders')
        if id == '0':
            order_menu()
        print('')
        customer_order = app_databases.read_from_database(f'SELECT p.product_id, p.product_name, p.product_price FROM customer_orders c JOIN products p ON c.product_id = p.product_id WHERE c.order_id = {id}')
        app_databases.print_order_table(customer_order) 
        input('\nPress Enter to continue.')       
        order_menu()
    elif option == '2':
        app_utilities.app_title()
        app_databases.add_to_database_function('orders')
        order_menu()
    elif option == '3':
        app_utilities.app_title()
        app_databases.update_order_status()
        order_menu()
    elif option == '4':
        app_utilities.app_title()
        app_databases.update_database_function('orders')
        order_menu()
    elif option == '5':
        app_utilities.app_title()
        app_databases.update_basket()
        order_menu()
    elif option == '6':
        app_utilities.app_title()
        app_databases.remove_database_function('orders')
        order_menu()
    elif option == '7':
        main_menu()
    elif option == '8':
        app_functions.exit_app()
    else:
        app_functions.incorrect_input()
        time.sleep(1)
        order_menu()
    
app_utilities.app_title()
app_functions.welcome_app()
app_utilities.app_title()
main_menu()
