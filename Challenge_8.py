# CHALLENGE NUMBER 8
# TOPIC: Lists
# Grocery List App.
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060744#overview

from datetime import datetime


def grocery_app():

    now = datetime.now()
    dt_string = now.strftime("%d/%m %H:%M")
    grocery_list = ['Meat', 'Cheese']

    print("Welcome to the Grocery List App.")
    print("Current Date and Time: " + dt_string)
    print("You currently have Meat and Cheese in your list.\n")

    for i in range (0,3):
        food = input("Type of food to add to the grocery list: ").title()
        grocery_list.append(food)

    print("\nHere is your grocery list:")
    print(grocery_list)
    grocery_list.sort()
    print("Here is your grocery list sorted:")
    print(grocery_list)
    print("\nSimulating grocery shopping...")

    for i in range (0,3):
        print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
        print(grocery_list)
        food_gone = input("What food did you just buy: ").title()
        print("Removing " + food_gone + " from list")
        grocery_list.remove(food_gone)

    print("Curent grocery list: " + str(len(grocery_list)) + " items")
    print(grocery_list)
    print("Sorry, the store is out of Meat")
    new_food = input("What food would you like instead: ").title()
    grocery_list.append(new_food)
    print("\nHere is what remains on your grocery list: ")
    print(grocery_list)

    return


if __name__ == '__main__':
    grocery_app()