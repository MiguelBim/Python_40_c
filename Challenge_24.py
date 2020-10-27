# CHALLENGE NUMBER 24
# TOPIC: Dic Struct
# Frequency Analysis App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060826#overview

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


if __name__ == '__main__':

    print("Welcome to the Frequency Analysis App")

    first_phrase = input("\nEnter a word of phrase to count the occurrence of each letter: ").lower()
    print("\nHere is the frequency analysis from key phrase 1:")
    frequency_analysis(first_phrase)

    second_phrase = input("\nEnter a word of phrase to count the occurrence of each letter: ").lower()
    print("\nHere is the frequency analysis from key phrase 2:")
    frequency_analysis(second_phrase)