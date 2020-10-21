# CHALLENGE NUMBER 19
# TOPIC: Conditional
# Voter Guess My Number
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060810#overview

import random


def guess_my_number(user_name):

    print("Well {}, I am thinking of a number between 1 and 20.".format(user_name))
    num_to_guess = random.randint(1,20)

    for guess_num in range(1,6):
        guess = int(input("\nTake a guess: ").strip())
        if guess == num_to_guess:
            print("Good job, {}! You guessed my number in {} guesses!".format(user_name, guess_num))
            return
        elif guess < num_to_guess:
            print("Your guess is too low.")
        elif guess > num_to_guess:
            print("Your guess is too high.")
        else:
            print("That's not a correct entry")
    print("\nGame Over. The number I was thinking of was {}.".format(num_to_guess))

    return


if __name__ == '__main__':

    print("Welcome to the Guess My Number App")
    name = input("\nHello! What is your name: ").title().strip()
    guess_my_number(name)