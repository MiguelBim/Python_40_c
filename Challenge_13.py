# CHALLENGE NUMBER 13
# TOPIC: For loop
# Factorial Calculator App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060780#overview

import math


def factorial_calculator(num):

    result_2 = 1

    print(str(num) + "! = ", end="")
    for val in range(1, num + 1):
        if val != num:
            print(str(val) + "*", end="")
        else:
            print(str(val))

        result_2 *= val

    result_1 = math.factorial(num)
    print("\nHere is the result from the math library:")
    print("The factorial of " + str(num) + " is " + str(result_1))

    print("\nHere is the result from my own algorithm:")
    print("The factorial of " + str(num) + " is " + str(result_2))

    print("\nIt is shown twice that " + str(num) + "! = " + str(result_1) + " (with excitement)")



    return


if __name__ == '__main__':
    print("Welcome to the Factorial Calculator App")
    num = int(input("\nWhat number would you like to compute the factorial of? "))
    factorial_calculator(num)