# CHALLENGE NUMBER 30
# TOPIC: Funct
# Dice App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060876#overview
import random


def dice_app(num_of_dice, roll_times):

    total_count = 0
    print("\n-----Results are as followed-----")
    for rolling in range(roll_times):
        val_from_rolling = random.randint(1, num_of_dice)
        print("\t\t{}".format(val_from_rolling))
        total_count += val_from_rolling
    print("The total value of your roll is {}.".format(total_count))

    return


if __name__ == '__main__':
    print("Welcome to the Python Dice App")

    run_app = True

    while run_app:
        dice_sides = int(input("\nHow many sides would you like on your dice: ").strip())
        dice_number = int(input("How many dice would you like to roll: "))
        print("\nYou rolled {} {} side dice.".format(dice_number, dice_sides))
        dice_app(dice_sides,dice_number)
        play_again = input("\nWould you like to roll again (y/n): ").lower().strip()
        if play_again == 'n':
            run_app = False
            print("Thank you")
        elif play_again != 'y':
            run_app = False
            print('\nThat is not a valid option. Exiting from app.')