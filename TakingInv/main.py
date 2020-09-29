from inventory import Inventory
from os import system

def main():
    answer = -1 
    while answer != 0:
        display_options()
        try:
            answer = int(input('Insert a number: '))
            system('clear')
        except ValueError:
            system('clear')
            print('Not a valid input\n')

        if answer == 1:
            add_item()

def display_options():
    print('''\nWhat would you like to do?
    1) Add a new item
    2) Adjust aspects for item
    3) Search for an item
    4) Delete an item
    0) Exit the Program\n''')

# Should create a new instance of the class
def add_item():
    try:
        item_department = int(input("Please enter department number:\n"))
        item_category = int(input("Please enter category number:\n"))
        item_style = int(input("Please enter 6-digit style number:\n"))
        item_price = float(input("Please enter the price of the item:\n$"))
        item_desc = input("Please enter a brief description of the item:\n")
    except ValueError:
        system('clear')
        print('Not a valid input\n')
        add_item()
    
    # This is where it adds the item to the stack but we haven't gotten that far yet so we're just going to display the class itself lmaooooo
    system('clear')
    item = Inventory(item_department, item_category, item_style, item_price, item_desc)
    item.display_info()

main()
