from random import randint
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

        if dice_choice == 1:
            dice_roll(4)
        elif dice_choice == 2:
            dice_roll(6)
        elif dice_choice == 3:
            dice_roll(8)
        elif dice_choice == 4:
            dice_roll(10)
        elif dice_choice == 5:
            dice_roll(12)
        elif dice_choice == 6:
            dice_roll(20)
        elif dice_choice == 7:
            dice_roll(100)
        elif dice_choice == 8:
            system('clear')
            print('\nGoodbye now!\n')
            exit()
        else:
            system('clear')
            print('Value Error: Inputs must be numbered 1-7\n')
            main()

# Rolls the dice, what else did you think it did, magic?
def dice_roll(top):
    adv_disadv = input('Are you at Advantage or Disadvantage?\n\t(A/D/NA)\n\n:')
    roll = randint(1, top)
    second_roll = randint(1, top)
    system('clear')
    if adv_disadv.upper() == 'A':
        if roll > second_roll or roll == second_roll:
            print('\nYou rolled a {}\n'.format(roll))
        elif second_roll > roll:
            print('\nYou rolled a {}\n'.format(second_roll))
    elif adv_disadv.upper() == 'D':
        if roll < second_roll or roll == second_roll:
            print('\nYou rolled a {}\n'.format(roll))
        elif second_roll < roll:
            print('\nYou rolled a {}\n'.format(second_roll))
    elif adv_disadv.upper() == 'NA':
        print('\nYou rolled a {}\n'.format(roll))
    else:
        system('clear')
        print('Please enter a valid input')
        dice_roll(top)

main()