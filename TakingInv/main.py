from inventory import Inventory
from os import system

available_departments = (8, 11, 12, 13, 14, 17, 21, 22, 24)


def main():
    answer = -1 
    while answer != 0:
        display_options_main()
        try:
            answer = int(input('Insert a number: '))
            system('clear')
        except ValueError:
            system('clear')
            print('Not a valid input\n')

        if answer == 1:
            add_item()
        if answer == 2:
            adjust_item()
        if answer == 3:
            search_item()
        if answer == 4:
            delete_item()

def display_options_main():
    print('''\nWhat would you like to do?
    1) Add a new item
    2) Adjust aspects for item
    3) Search for an item
    4) Delete an item
    0) Exit the Program\n''')

def display_options_adjust():
    print('''What would you like to adjust?
    1) Department Number
    2) Category Number
    3) Style Number
    4) Item Price
    5) Item Description
    0) Return to options menu''')

# Should create a new instance of the class
def add_item():
    try:
        item_department = int(input("Please enter department number:\n"))
        if item_department not in available_departments:
            raise ValueError
        
        item_category = int(input("Please enter category number:\n"))
        if len(str(item_category)) != 4:
            raise ValueError

        item_style = int(input("Please enter 6-digit style number:\n"))
        if len(str(item_style)) != 6:
            raise ValueError

        item_price = float(input("Please enter the price of the item:\n$"))
        if str(item_price)[-2:] != "00" and str(item_price)[-2:] != "99":
            raise ValueError
        
        item_desc = input("Please enter a brief description of the item:\n")
    except ValueError:
        system('clear')
        print('Not a valid input\n')
        add_item()
    
    # This is where it adds the item to the stack but we haven't gotten that far yet so we're just going to display the class itself lmaooooo
    system('clear')
    item = Inventory(item_department, item_category, item_style, item_price, item_desc)
    item.display_info()

def adjust_item():
    answer = -1
    while answer != 0:
        display_options_adjust()
        try:
            answer = int(input('Insert a Number'))
            system('clear')
        except ValueError:
            print('That is not a valid input')
            system('clear')
            adjust_item()
        


# To be written later
def search_item(): 
    pass

def delete_item():
    pass

main()
