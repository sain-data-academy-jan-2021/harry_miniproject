import os, sys

# Basic Functions


def clear():
    os.system("clear")


def print_list(list):
    for value in list:
        print(value)


def app_title():
    clear()
    title = " * THE JAMMIE DODGER CAFE * "
    title_length = len(title)
    print("*" * title_length)
    print(title)
    print("*" * title_length + "\n")


def welcome_app():
    input("Welcome to the Jammie Dodger Cafe!\n\nPress enter to continue: ... ")


def menu_title(menu):  # idea for future use
    title = menu
    title_length = len(title)
    print("*" * title_length)
    print(title)
    print("*" * title_length + "\n")


def exit_app():
    clear()
    app_title()
    print("Thank you for visiting the Jammie Dodger Cafe!\n")
    sys.exit()


def incorrect_input():
    input("Input not recognised. Returning to previous screen: ... ")


def last_num(list):
    last_num = int(list[-1]["Index"])
    last_num += 1
    return str(last_num)


# List Functions


def show_list(list):
    print_list(list)
    input("\nPress any key to continue: ... ")
    return


def add_to_list(item, list):
    if 'product' in item:
        try:
            product_name = input(
                "Enter 0 to cancel.\n\nWhat is the name of the product you would like to add?: ... "
            ).capitalize()
            if product_name == "0":
                return []
            else:
                product_price = input(
                    "\nWhat is the price of this new product?: ... "
                ).strip("£")
                if product_price == "0":
                    return []
                else:
                    product_price = float(product_price)
                    list.append(
                        {
                            "Index": last_num(list),
                            "Name": product_name,
                            "Price": product_price,
                        }
                    )
                    app_title()
                    for x in list:
                        print(x)
                    input(
                        "\nThe product has been successfully added.\nPress enter to continue."
                    )
                    return list

        except ValueError:
            app_title()
            input(
                "The price format could not be read.\nPlease enter the price in the format '1.00'\n\nPress enter to continue."
            )

    elif "courier" in item:
        courier_name = input(
            "Enter 0 to cancel.\n\nWhat is the name of the courier you would like to add?: ... "
        ).capitalize()
        if courier_name == "0":
            return []
        else:
            courier_number = input("\nWhat is the courier's mobile number?: ... ")
            if courier_number == "0":
                return []
            else:
                if len(courier_number) != 11:
                    app_title()
                    input(
                        "This phone number is not a valid length.\nPress enter to continue."
                    )
                else:
                    app_title()
                    list.append(
                        {
                            "Index": last_num(list),
                            "Name": courier_name,
                            "Phone Number": courier_number,
                        }
                    )
                    app_title()
                    for x in list:
                        print(x)
                    input(
                        "\nThe courier has been successfully added.\nPress enter to continue."
                    )
                    return list


def update_item_in_list(product_or_courier, secondary_info, list):
        for x in list:
            print(x)
        index_choice = input(f'\nEnter 0 to cancel.\n\nWhat is the index of the {product_or_courier} you would like to update?: ... ').capitalize()
        if index_choice == '0':
            return []
        else:
            index = int(index_choice)
            app_title()
            print('Leave blank and press enter if you do not want to update')
            first_value = input('\nWould you like to update the name?: ... ').capitalize()
            if first_value == '':
                pass
            else:
                list[index - 1]['Name'] = first_value
            second_value = input(f'Would you like to update the {secondary_info}?: ... ').capitalize()
            if second_value == '':
                pass
            else:
                list[index - 1][secondary_info] = second_value
            for x in list:
                print(x)
            input(f"\n{product_or_courier.capitalize()} {index_choice} has been updated.\nPress enter to continue: ... ")
            return list

def remove_item_in_list(product_or_courier, list):
        for x in list:
            print(x)
        index_choice = input(f'\nEnter 0 to cancel.\n\nWhat is the index of the {product_or_courier} you would like to remove?: ... ').capitalize()
        if index_choice == '0':
            return []
        elif len(list) == 0:
            input(f"There is no {product_or_courier} to remove.\nPress enter to continue: ... ")
        else:
            index = int(index_choice)
            del list[index - 1]
            for x in list:
                print(x)
            input(f"\n{product_or_courier.capitalize()} {index_choice} has been removed.\nPress enter to continue: ... ")
            return list



# Dictionary Functions


def show_dict(dictionary):
    for key, value in dictionary.items():
        print(key, value)
    input("\nPress any key to continue: ... ")


def add_dict(dictionary):
    for order in dictionary:
        print(order)
    order_no = input("\nPress 0 to cancel.\nEnter new order number: ... ")

    if order_no == "0":
        return {}

    elif order_no in dictionary:
        input(f"\nThis order number already exists.\nPress enter to continue: ... ")

    else:
        app_title()
        forming_dict = {}

        first_name = input("What is your first name?: ... ").title()
        forming_dict["First Name"] = first_name

        last_name = input("What is your last name?: ... ").title()
        forming_dict["Last Name"] = last_name

        customer_address = input("What is your address?: ... ").title()
        forming_dict["Customer Address"] = customer_address

        customer_number = input("What is your phone number?: ... ")
        forming_dict["Customer Number"] = customer_number

        courier = input("Which courier would you like?: ... ").title()
        forming_dict["Courier"] = courier

        forming_dict["Status"] = "Preparing"

        dictionary[order_no] = {
            "First Name": first_name,
            "Last Name": last_name,
            "Customer Address": customer_address,
            "Customer Number": customer_number,
            "Courier": courier,
            "Status": "Preparing",
        }
        app_title()
        print(dictionary[order_no])
        forming_dict.clear()
        input("\nYour details have been added.\nPlease enter to continue: ... ")
        return dictionary


def update_status(dictionary):
    for order in dictionary:
        print(order)
    order_num = input(
        "\nPress 0 to cancel.\nWhich order would you like to update the status of?: ... "
    ).title()

    if order_num == "0":
        return {}

    elif order_num in dictionary:
        app_title()
        dictionary[order_num]["Status"] = "Ready"
        input("This orders status has been updated.\nPress enter to continue: ... ")
        return dictionary

    elif len(dictionary) == 0:
        app_title()
        input("There are no orders to update.\nPress enter to continue: ... ")

    else:
        app_title()
        input(f"{order_num} isn't an order number.\nPress enter to continue: ... ")


def update_dictionary(dictionary):
    for order in dictionary:
        print(order)
    order_option = input(
        "\nPress 0 to cancel.\nWhich order would you like to update: ... "
    )

    if order_option == "0":
        return {}

    elif order_option in dictionary:
        app_title()
        print("Leave blank and press enter if you do not want to update:\n")

        first_name = input("Would you like to update your first name?: ... ").title()
        if first_name == "":
            pass
        else:
            dictionary[order_option]["First Name"] = first_name

        last_name = input("Would you like to update your last name?: ... ").title()
        if last_name == "":
            pass
        else:
            dictionary[order_option]["Last Name"] = last_name

        customer_address = input("Would you like to update your address?: ... ").title()
        if customer_address == "":
            pass
        else:
            dictionary[order_option]["Customer Address"] = customer_address

        customer_number = input("Would you like to update your phone number?: ... ")
        if customer_number == "":
            pass
        else:
            dictionary[order_option]["Customer Number"] = customer_number

        courier = input("Would you like to update the courier?: ... ").title()
        if courier == "":
            pass
        else:
            dictionary[order_option]["Courier"] = courier

        input(f"\n{order_option} has been updated.\nPress enter to continue: ... ")
        return dictionary


def remove_dictionary(dictionary):
    for order in dictionary:
        print(order)
    option = input(
        "\nPress 0 to cancel.\nWhich order would you like to remove?: ... "
    ).title()

    if option == "0":
        return {}

    elif len(dictionary) == 0:
        input("There are no orders to remove.\nPress any key to continue: ... ")

    elif option in dictionary:
        app_title()
        del dictionary[option]

        for order in dictionary:
            print(order)
        input(f"\n{option} has been removed.\nPress any key to continue: ... ")

    else:
        app_title()
        input(f"{option} isn't an order number.\nPress any key to continue: ... ")
