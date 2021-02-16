import csv

product_information = []
courier_information = []
order_information = []

# Data Persistence w/ Dictionaries in Lists


def import_data_from_list(filename, list):  # filename needs to be passed as 'filename.csv'
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
        elif "order" in filename:
            fieldnames = ["Index", "First Name", "Last Name", "Customer Address", "Customer Number", "Courier", "Status"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow(row)

# Imports the files for the main code when it is run
import_data_from_list("list_data/product_information.csv", product_information)
import_data_from_list("list_data/courier_information.csv", courier_information)
import_data_from_list("list_data/order_information.csv", order_information)

