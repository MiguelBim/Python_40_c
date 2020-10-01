# CHALLENGE NUMBER 5
# Multiplication/Exponent Table
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060728#overview

# NOTES


def calculate_multiplication(number):

    print("\nMultiplication Table For " + number + "\n")

    for n in range(1,10):
        result = float(number) * n
        print(str(round(float(n),1)) + " * " + str(round(float(number),2)) + " = " + str(round(result,2)))

    return


def calculate_exponent(number):

    print("\nExponent Table For " + number + "\n")

    for n in range(1,10):
        result = float(number) ** n
        print(str(round(float(number),2)) + str(float(n)) + " * " + " = " + str(round(result,4)))

    return


if __name__ == '__main__':

    print("Welcome to the Multiplication/Exponent Table App")
    username = input("Hello, what is your name:\t").title().strip()
    number = input("What number would you like to work with: ")
    message = "math is cool!"

    calculate_multiplication(number)
    calculate_exponent(number)

    print("\n" + username.title() + " " + message.capitalize())
    print("\t" + username.lower() + " " + message.lower() )
    print("\t\t" + username.capitalize() + " " + message.title() )
    print("\t\t\t" + username.upper() + " " + message.upper() )