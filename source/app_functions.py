import os, time, sys, app_databases, app_utilities
os.system('clear')


def print_list(list):
    for value in list:
        print(value) 


def exit_app():
    os.system('clear')
    app_utilities.app_title()
    print("Thank you for visiting the Jammie Dodger Cafe!\n")
    app_databases.disconnect_from_database()
    sys.exit()


def welcome_app():
    print("Welcome to the Jammie Dodger Cafe!")
    time.sleep(1.5)


def incorrect_input():
    print("Input not recognised. Returning to previous screen: ... ")
    time.sleep(1.5)

def index_choice(process):
    print('\nPress 0 to cancel operation.')
    index_choice = input(f'\nWhat is the index of the data you want to {process}?: ... ')
    if index_choice == '0':
        return '0'
    else:
        index = int(index_choice) - 1
        return index


def last_num(list):
    if list == []:
        last_num = 1
    else:
        last_num = int(list[-1]["Index"])
        last_num += 1
    return str(last_num) 


def show_list(list):
    print_list(list)
    input('Enter any key to continue. ')


def validate_entries(new_value, key, list, type):
    if key == 'Phone Number':
        if len(new_value) == 11:
            return
        else:
            app_utilities.app_title()
            print('The Phone Number cannot be recognised.\nThe Phone Number must be 11 digits long.\n')
            if type == 'add':
                add_to_list(list)
            
#     elif key == 'Price':
#         try:
#             Prices value == float(prices value)
#             continue
#         except Exception as e:
#             print('The Price is cannot be recognised.\n The Price should be in the format x.xx')
#         finally:
#             return to previous screen?


def add_to_list(list):
    print_list(list)
    print('\nPress 0 to cancel operation.')
    updated_dict = add_list_operation(list)
    if updated_dict ==  None:
        return
    else: # not needed because the rest of the program should run anyway
        list.append(updated_dict)
        app_utilities.app_title()
        print(f'You have successfully updated the information.\n')
        print_list(list)
        time.sleep(3)
        return list


def add_list_operation(list):
    forming_dict = {}
    forming_dict.update({'Index': last_num(list)})
    for key in list[0]:
        if key == 'Index':
            pass
        elif key == 'Status':
            forming_dict.update({'Status': 'Preparing'})
        else:
            new_value = input(f'\nWhat value would you like to add for the {key.lower()}?: ... ').capitalize()
            if new_value == '0':
                return
            else:
                validate_entries(new_value, key, list, 'add')
                forming_dict.update({key: new_value})
    return forming_dict


def update_list_operation(list, index, key, new_value):
    list[index][key] = new_value
    return list


def update_list(list):
    print_list(list)
    index = index_choice('update')
    if index == '0':
        return
    else:
        app_utilities.app_title()
        print('Press 0 to cancel operation.')
        print('Leave blank and press enter if you do not want to update.\n')
        
        for key in list[index]:
            if key == 'Index' or key == 'Status':
                pass
            else:
                new_value = input(f'\nWhat would you like to replace the {key.lower()} with?: ... ').capitalize()
                if new_value == '0':
                    return
                elif new_value == '':
                    pass
                else:
                    update_list_operation(list, index, key, new_value)
                    
        app_utilities.app_title()
        print('The list has been updated with your changes.\n')
        print_list(list)
        time.sleep(3)
        return list
     
        
def remove_list_operation(list, index):
    del list[index]
    return list


def remove_from_list(list):
    print_list(list)
    index = index_choice('remove')
    if index == '0':
        return
    else:
        remove_list_operation(list, index)
        app_utilities.app_title()
        print('The list has been updated with your changes.\n')
        print_list(list)
        time.sleep(3)
        return list


def update_order_status(list):
    print_list(list)
    order_status = ['Preparing', 'Cancelled', 'Out for delivery', 'Delivered']
    index = index_choice('update')
    app_utilities.app_title()
    print(order_status)
    status_choice = input('\nPick a status to change the order to: ... ').capitalize()
    if status_choice in order_status:
        update_order_status_operation(list, index, status_choice)
        app_utilities.app_title()
        print('The list has been updated with your changes.\n')
        print_list(list)
        time.sleep(3)
        return list
    else:
        print("The order could not be updated.")
        time.sleep(3)
        return list


def update_order_status_operation(list, index, status_choice):
    list[index]['Status'] = status_choice
    return list


def order_basket(list):
    basket = []
    print_list(list)
    order_selection = input('Please select products from the menu using the index number.\nSeparate multiple items with a comma and space: ... ')
    separated_product_list = order_selection.split(', ')
    for item in separated_product_list:
        basket.append(item)
    return basket