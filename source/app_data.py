import csv

product_information = []
courier_information = []
fields = [
    "Order",
    "First Name",
    "Last Name",
    "Customer Address",
    "Customer Number",
    "Courier",
    "Status",
]
order_dictionary = {}

# Data Persistence w/ Dictionaries in Lists


def import_data_from_list(
    filename, list
):  # filename needs to be passed as 'filename.csv'
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


# Data Persistence w/ Dictionaries in Dictionaries


def import_data_dict():
    with open("list_data/order_dict.csv", "r") as data_file:
        data = csv.DictReader(data_file)
        for row in data:
            key = row["Order"]
            del row["Order"]
            order_dictionary[key] = row
            for key, value in order_dictionary.items():
                print(key, value)


def export_data_dict():
    with open("list_data/order_dict.csv", "w") as file:  # writing to the file
        writer = csv.DictWriter(file, fields)
        writer.writeheader()
        for key, value in order_dictionary.items():
            row = {"Order": key}
            row.update(value)
            writer.writerow(row)


# Imports the files for the main code when it is run
import_data_from_list("list_data/product_information.csv", product_information)
import_data_from_list("list_data/courier_information.csv", courier_information)
import_data_dict()
