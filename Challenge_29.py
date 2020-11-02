# CHALLENGE NUMBER 28
# TOPIC: While Struct
# Guess de word app
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060862#overview
import random


def guess_word():

    categories = {
        1: ['sports_list', 'soccer', 'football', 'tennis', 'rugby', 'running'],
        2: ['fruits_list', 'apple', 'orange', 'banana', 'watermelon', 'tangerine'],
        3: ['cars_list', 'audi', 'ferrari', 'mclaren', 'mazda', 'bmw'],
        4: ['countries_list', 'mexico', 'canada', 'india', 'colombia', 'london']
    }
    category_num = random.randint(1, 4)
    category_values = categories[category_num][1:]
    word_num = random.randint(0, len(category_values) - 1)
    print("\nGuess a {} letter word from the following category: {}".format(len(category_values[word_num]), categories[category_num][0]))
    print('-'*len(category_values[word_num]))

    guess_counter = 1
    run_guess = True
    hidden_word = ['-']*len(category_values[word_num])
    while run_guess:
        uncover_letter = True
        user_guess = input("\nEnter your guess: ")
        if user_guess.lower().strip() == category_values[word_num]:
            print("\nCorrect! You guessed the word in {} guesse(s).".format(guess_counter))
            run_guess = False
        else:
            print("That is not correct. Let us reveal a letter to help you!")
            while uncover_letter:
                word_ind = random.randint(0, len(hidden_word) - 1)
                if hidden_word[word_ind] == '-':
                    hidden_word[word_ind] = category_values[word_num][word_ind]
                    uncover_letter = False
                else:
                    continue
            print("".join(hidden_word))
            guess_counter += 1


if __name__ == '__main__':

    print("Welcome to the Guess My Word App")
    run_program = True
    while run_program:
        guess_word()
        user_option = input("Would you like to play again (y/n): ").strip().lower()
        if user_option == 'n':
            print("\nThank you for playing our game")
            run_program = False
        else:
            continue