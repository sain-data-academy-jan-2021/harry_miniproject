import app_functions, sys, os, app_data
from app_data import (
    product_information,
    courier_information,
    order_dictionary,
)


def continue_option(menu):
    if menu == "courier_menu":
        var_1 = "courier menu"
    elif menu == "product_menu":
        var_1 = "product menu"
    elif menu == "order_menu":
        var_1 = "order menu"

    cont_option = input(
        f"1)\tContinue using the {var_1}\n2)\tReturn to the main menu\n3)\tExit the app\n\nWhat would you like to do?: ... "
    )
    if cont_option == "1":
        if menu == "courier_menu":
            app_functions.app_title()
            courier_menu()
        elif menu == "product_menu":
            app_functions.app_title()
            product_menu()
        elif menu == "order_menu":
            app_functions.app_title()
            order_menu()
    elif cont_option == "2":
        app_functions.app_title()
        main_menu()
    elif cont_option == "3":
        app_functions.exit_app()


def main_menu():
    print("1)\tProduct Menu\n2)\tCourier Information\n3)\tOrder Menu\n4)\tExit App\n")
    main_choice = input("Please select an option: ... ")
    if main_choice == "1":
        app_functions.app_title()
        product_menu()

    elif main_choice == "2":
        app_functions.app_title()
        courier_menu()

    elif main_choice == "3":
        app_functions.app_title()
        order_menu()

    elif main_choice == "4":
        app_functions.exit_app()
    else:
        app_functions.incorrect_input()
        app_functions.app_title()
        main_menu()


def product_menu():
    print(
        "1)\tShow Menu\n2)\tAdd to Menu\n3)\tUpdate Menu\n4)\tRemove from Menu\n5)\tMain Menu\n"
    )
    product_choice = input("Please select an option: ... ")
    
    if product_choice == "1":
        app_functions.app_title()
        app_functions.show_list(product_information)
        app_functions.app_title()
        product_menu()

    elif product_choice == "2":
            app_functions.app_title()
            response = app_functions.add_to_list("product", product_information)
            if not response:
                app_functions.app_title()
                product_menu()
            else:
                app_data.export_data_from_list(
                    "list_data/product_information.csv", product_information
                )
                app_functions.app_title()
                continue_option("product_menu")

    elif product_choice == "3":
            app_functions.app_title()
            response = app_functions.update_item_in_list('product', 'price', product_information)
            if not response:
                app_functions.app_title()
                product_menu()
            else:
                app_data.export_data_from_list(
                    "list_data/product_information.csv", product_information)
                app_functions.app_title()
                continue_option("product_menu")

    elif product_choice == "4":
            app_functions.app_title()
            response = app_functions.remove_item_in_list('product', product_information)
            if not response:
                app_functions.app_title()
                product_menu()
            else:
                app_data.export_data_from_list(
                    "list_data/product_information.csv", product_information
                )
                app_functions.app_title()
                continue_option("product_menu")

    elif product_choice == "5":
        app_functions.app_title()
        main_menu()

    else:
        app_functions.incorrect_input()
        app_functions.app_title()
        product_menu()


def courier_menu():
    print(
        "1)\tShow Courier List\n2)\tAdd a New Courier\n3)\tUpdate a Courier\n4)\tRemove a Courier\n5)\tMain Menu\n"
    )
    courier_menu_choice = input("Please select an option: ... ")

    if courier_menu_choice == "1":
        app_functions.app_title()
        app_functions.show_list(courier_information)
        app_functions.app_title()
        courier_menu()

    elif courier_menu_choice == "2":
        app_functions.app_title()
        response = app_functions.add_to_list("courier", courier_information)
        if not response:  # try to throw out the same objects
            app_functions.app_title()
            courier_menu()
        else:
            app_data.export_data_from_list(
                "courier_information.csv", courier_information
            )
            app_functions.app_title()
            continue_option("courier_menu")

    elif courier_menu_choice == "3":
        app_functions.app_title()
        response = app_functions.update_item_in_list('courier', 'phone number', courier_information)
        if not response:
            app_functions.app_title()
            courier_menu()

        else:
            app_data.export_data_from_list(
                "courier_information.csv", courier_information
            )
            app_functions.app_title()
            continue_option("courier_menu")

    elif courier_menu_choice == "4":
        app_functions.app_title()
        response = app_functions.remove_item_in_list('courier', courier_information)
        if not response:
            app_functions.app_title()
            courier_menu()

        else:
            app_data.export_data_from_list(
                "courier_information.csv", courier_information
            )
            app_functions.app_title()
            continue_option("courier_menu")

    elif courier_menu_choice == "5":
        app_functions.app_title()
        main_menu()

    else:
        app_functions.incorrect_input()
        app_functions.app_title()
        courier_menu()


def order_menu():
    print(
        "1)\tShow Order List\n2)\tAdd a New Order\n3)\tUpdate an Order Status\n4)\tUpdate an Order\n5)\tRemove an Order\n6)\tMain Menu\n"
    )
    order_menu_choice = input("Please select an option: ... ")

    if order_menu_choice == "1":
        app_functions.app_title()
        app_functions.show_dict(order_dictionary)
        app_functions.app_title()
        order_menu()

    elif order_menu_choice == "2":
        app_functions.app_title()
        response = app_functions.add_dict(order_dictionary)
        if not response:
            app_functions.app_title()
            order_menu()
        else:
            app_data.export_data_dict()
            app_functions.app_title()
            continue_option("order_menu")

    elif order_menu_choice == "3":
        app_functions.app_title()
        response = app_functions.update_status(order_dictionary)
        if not response:
            app_functions.app_title()
            order_menu()
        else:
            app_data.export_data_dict()
            app_functions.app_title()
            continue_option("order_menu")

    elif order_menu_choice == "4":
        app_functions.app_title()
        response = app_functions.update_dictionary(order_dictionary)
        if not response:
            app_functions.app_title()
            order_menu()
        else:
            app_data.export_data_dict()
            app_functions.app_title()
            continue_option("order_menu")

    elif order_menu_choice == "5":
        app_functions.app_title()
        response = app_functions.remove_dictionary(order_dictionary)
        if not response:
            app_functions.app_title()
            order_menu()
        else:
            app_data.export_data_dict()
            app_functions.app_title()
            continue_option("order_menu")

    elif order_menu_choice == "6":
        app_functions.app_title()
        main_menu()

    else:
        app_functions.incorrect_input()
        app_functions.app_title()
        order_menu()


# Run app
app_functions.app_title()
app_functions.welcome_app()
app_functions.app_title()
main_menu()