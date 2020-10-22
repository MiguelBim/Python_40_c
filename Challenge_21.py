# CHALLENGE NUMBER 21
# TOPIC: Dic Struct
# Thesaurus App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060816#overview

import random


def thesaurus_app(word, dictionary):

    rand_num = random.randint(0, 4)
    app_response = dictionary[word][rand_num]
    print("A synonym for {} is {}.".format(word, app_response))

    see_dict = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()

    if see_dict == "yes":
        for key, values in dictionary.items():
            print("\n{} synonyms are: ".format(key.title()))
            for value in values:
                print("\t\t- {}".format(value))
    elif see_dict == "no":
        print("\nI hope you enjoyed the program. Thank you!")
    else:
        print("\nThat entry is not valid, exiting from the thesaurus app.")

    return


if __name__ == '__main__':

    thesaurus_dict = {
        "hot": ["balmy", "summery", "tropical", "boiling", "scorching"],
        "cold": ["chilly", "cool", "freezing", "frigid", "polar"],
        "happy": ["content", "cheery", "merry", "jovial", "jocular"],
        "sad": ["unhappy", "downcast", "miserable", "glum", "melancholy"]
    }

    print("Welcome to the Thesaurus App!")
    print("\nChoose a word from the thesaurus and I will give you a synonym.")
    print("\nHere are the words in the thesaurus: ")
    for key in thesaurus_dict.keys():
        print("\t-{}".format(key))

    entered_word = input("\nWhat word would you like a synonym for: ").lower().strip()
    if entered_word in thesaurus_dict.keys():
        thesaurus_app(entered_word, thesaurus_dict)
    else:
        print("I'm sorry, that word is not in thesaurus app. Try again!")

