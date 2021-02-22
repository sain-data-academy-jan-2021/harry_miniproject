import os, time, sys, app_databases, app_utilities
os.system('clear')

def exit_app():
    os.system('clear')
    app_utilities.app_title()
    print("Thank you for visiting the Jammie Dodger Cafe!\n")
    app_databases.disconnect_from_database()
    sys.exit()


def welcome_app():
    print("Welcome to the Jammie Dodger Cafe!")
    time.sleep(1)


def incorrect_input():
    print("Input not recognised. Returning to previous screen: ... ")
    time.sleep(0.5)
