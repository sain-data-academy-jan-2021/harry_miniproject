import time, app_menu_displays, app_functions, app_data, app_databases, app_utilities
from app_data import product_information, courier_information, order_information


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
        time.sleep(1.5)
        main_menu()

def product_menu():
    app_utilities.app_title()
    option = app_menu_displays.product_menu_display()
    if option == '1':
        app_utilities.app_title()
        app_databases.print_table_function('products')
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
        time.sleep(1.5)
        product_menu()

def courier_menu():
    app_utilities.app_title()
    option = app_menu_displays.courier_menu_display()
    if option == '1':
        app_utilities.app_title()
        app_databases.print_table_function('couriers')
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
        time.sleep(1.5)
        product_menu()
        
def order_menu():
    app_utilities.app_title()
    option = app_menu_displays.order_menu_display()
    if option == '1':
        app_utilities.app_title()
        app_databases.print_table_function('orders')
        input('\nPress Enter to continue. ')
        order_menu()
    elif option == '2':
        app_utilities.app_title()
        app_databases.add_to_database_function('orders')
        # app_functions.add_to_list(order_information)
        # app_data.export_data_from_list("list_data/order_information.csv", order_information)
        order_menu()
    elif option == '3':
        app_utilities.app_title()
        app_functions.update_order_status(order_information)
        app_data.export_data_from_list("list_data/order_information.csv", order_information)
        order_menu()
    elif option == '4':
        app_utilities.app_title()
        app_functions.update_list(order_information)
        app_data.export_data_from_list("list_data/order_information.csv", order_information)
        order_menu()
    elif option == '5':
        app_utilities.app_title()
        app_functions.remove_from_list(order_information)
        app_data.export_data_from_list("list_data/order_information.csv", order_information)
        order_menu()
    elif option == '6':
        main_menu()
    elif option == '7':
        app_functions.exit_app()
    else:
        app_functions.incorrect_input()
        time.sleep(1.5)
        order_menu()
    
app_utilities.app_title()
app_functions.welcome_app()
app_utilities.app_title()
main_menu()
