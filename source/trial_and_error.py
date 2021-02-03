import os
import csv
os.system('clear')

def clear():
    os.system('clear')

def app_title():
    clear()
    title = ' * THE JAMMIE DODGER CAFE * '
    title_length = len(title)
    print('*' * title_length)
    print(title)
    print('*' * title_length + '\n')

def demo_def(): 
    doesthiswork = input('Does this work?')
    if doesthiswork == 'yes':
        return 'hurray'
    elif doesthiswork == 'no':
        return 'bummer'
    else:
        return 'something went wrong'