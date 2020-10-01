
# CHALLENGE NUMBER 1
# Word count
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060710#overview

def my_solution(message, letter):

    letter_dict = {}
    for character in message.lower():
        letter_dict[character] = letter_dict.get(character, 0) + 1

    return letter_dict[letter.lower()]


def instructor_solution(message, letter):

    message = message.lower()
    letter = letter.lower()
    letter_count = message.count(letter)
    return letter_count


if __name__ == '__main__':

    print("Welcome to the letter count App")
    name = input("What is your name?: ").title().strip()
    print("Hello, " + name)
    print("I will count the number of times that a specific letter occurs in a message. ")
    message = input("Please enter a message: ")
    letter = input("Which letter would you like to count the occurrences of?: ")
    # answer = my_solution(message, letter)
    answer = instructor_solution(message, letter)
    # print(answer)
    print(name + ", your message has " + str(answer) + " " + letter.lower() + "'s in it")