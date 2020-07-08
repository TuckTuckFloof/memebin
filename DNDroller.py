from random import randint, randrange
from os import system

def main():
    dice_choice = 0
    while dice_choice != 8: 
        print('Please choose the dice you will be rolling. \n'
            '1) D4\n'
            '2) D6\n'
            '3) D8\n'
            '4) D10\n'
            '5) D12\n'
            '6) D20\n'
            '7) D100\n'
            '8) Exit the Program\n\n')

        try:
            dice_choice = int(input(': '))
        except ValueError:
            # If you're running this on a windows system
            # Change 'clear' to 'cls'
            system('clear')
            print('ValueError: Inputs must be numbered 1-7')
            main()

        system('clear')

        if dice_choice == 1:
            print('You rolled a {}\n'.format(randint(1, 4)))
        elif dice_choice == 2:
            print('You rolled a {}\n'.format(randint(1, 6)))
        elif dice_choice == 3:
            print('You rolled a {}\n'.format(randint(1, 8)))
        elif dice_choice == 4:
            print('You rolled a {}\n'.format(randint(1, 10)))
        elif dice_choice == 5:
            print('You rolled a {}\n'.format(randint(1, 12)))
        elif dice_choice == 6:
            print('You rolled a {}\n'.format(randint(1, 20)))
        elif dice_choice == 7:
            print('You rolled a {}\n'.format(randrange(10, 100, 10)))
        elif dice_choice == 8:
            print('Goodbye now!\n')
            exit()
        else:
            system('clear')
            print('Value Error: Inputs must be numbered 1-7\n')
            main()

main()