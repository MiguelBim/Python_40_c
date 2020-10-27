# CHALLENGE NUMBER 25
# TOPIC: Dic Struct
# Code Breakers App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060828#overview

import string


def frequency_analysis(user_phrase):

    table = str.maketrans(dict.fromkeys(string.punctuation))
    strip_user_phrase = user_phrase.translate(table)
    format_phrase = strip_user_phrase.replace(" ", "")

    letters_dict = {}
    total_counter = 0

    for letter in format_phrase:
        counter = letters_dict.get(letter, 0) + 1
        letters_dict[letter] = counter
        total_counter += 1

    sorted_dict = dict(sorted(letters_dict.items()))
    print("\nLetter\t\tOccurrence\t\tPercentage")
    for letter, occurrence in sorted_dict.items():
        letter_percentage = round((occurrence * 100) / total_counter, 2)
        print("{}\t\t\t{}\t\t\t\t{}%".format(letter, occurrence, letter_percentage))

    print("\nLetters ordered from highest occurrence to lowest:")
    val_sorted_list = sorted(sorted_dict, key=sorted_dict.get, reverse=True)
    for letter in val_sorted_list:
        print(letter, end="")


def encode_app(original_phrase):

    encode_phrase = original_phrase.encode('utf-16')
    print("\nThe encoded message is: \n{}".format(encode_phrase))

    return


if __name__ == '__main__':

    print("Welcome to the Frequency Analysis App")

    phrase_one = "Thinking, Fast and Slow is a best-selling[1] book published during 2011 by Nobel Memorial Prize in Economic Sciences laureate Daniel Kahneman. It was the 2012 winner of the National Academies Communication Award for best creative work that helps the public understanding of topics of behavioral science, engineering and medicine.[2]"
    phrase_two = "The book summarizes research that Kahneman performed during decades, often in collaboration with Amos Tversky.[3][4] It covers all three phases of his career: his early work concerning cognitive biases, his work on prospect theory, and his later work on happiness."

    print("\nHere is the frequency analysis from key phrase 1:")
    frequency_analysis(phrase_one)
    print("\nHere is the frequency analysis from key phrase 2:")
    frequency_analysis(phrase_two)

    encode_ans = input("\n\nWould you like to encode a message (yes/no): ").lower().strip()
    if encode_ans == 'yes':
        phrase_to_encode = input("What is the phrase: ").lower().strip()
        encode_app(phrase_to_encode)
    elif encode_ans == 'no':
        print("Thanks for using this app!")
    else:
        print("Not a valid selection. Exiting now!")