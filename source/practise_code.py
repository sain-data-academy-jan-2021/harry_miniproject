import os
import csv

os.system("clear")
food_information = []
drink_information = []
couriers = []

def import_data_from_list(filename, list): # filename needs to be passed as 'filename.csv'
    with open(filename, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            list.append(row)

def export_data_from_list(filename, list):
    with open(filename, "w") as file:
        if "product" in filename:
            fieldnames = ["Index", "Name", "Price"]
        elif "courier" in filename:
            fieldnames = ["Index", "Name", "Phone Number"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow(row)

def clear():
    os.system("clear")


def app_title():
    clear()
    title = " * THE JAMMIE DODGER CAFE * "
    title_length = len(title)
    print("*" * title_length)
    print(title)
    print("*" * title_length + "\n")


def add_to_list(list):
    if list == food_information or list == drink_information:
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

    elif list == couriers:
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
                    couriers.append(
                        {
                            "Index": last_num(list),
                            "Name": courier_name,
                            "Phone Number": courier_number,
                        }
                    )
                    app_title()
                    for x in couriers:
                        print(x)
                    input(
                        "\nThe courier has been successfully added.\nPress enter to continue."
                    )
                    return list


def last_num(list):
    last_num = int(list[-1]["Index"])
    last_num += 1
    return str(last_num)


def printing_practise(list):
    index = 0
    for i in list:
        print(index + 1, list[index]["Name"], ":", list[index]["Price"])
        index += 1

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
            first_value = input('\nWould you like to update the name?: ... ')
            if first_value == '':
                pass
            else:
                list[index - 1]['Name'] = first_value
            second_value = input(f'Would you like to update the {secondary_info}?: ... ')
            if second_value == '':
                pass
            else:
                list[index - 1][secondary_info] = second_value
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
            input(f"\n{product_or_courier.capitalize()} {index_choice} has been updated.\nPress enter to continue: ... ")
            return list
            
products = [{'Index': '1', 'Name': 'Harry', 'Phone Number': '07518096938'}]

couriers =[]

app_title()
remove_item_in_list('courier', couriers)

print(products)