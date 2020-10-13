# CHALLENGE NUMBER 12
# TOPIC: For loop
# Quadratic Solver App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060778#overview

import cmath


def solve_equations(eq_num):

    for num in range(1, eq_num + 1):
        print("\nSolving equation #" + str(num))
        print("-" * 70)
        var_a = float(input("\nPlease enter the value of a (coefficient of x^2): "))
        var_b = float(input("Please enter the value of b (coefficient of x): "))
        var_c = float(input("Please enter the value of c (coefficient): "))

        # The Discriminant
        disc = (var_b ** 2) - (4 * var_a * var_c)

        # Solutions
        solution1 = (-var_b - cmath.sqrt(disc)) / (2 * var_a)
        solution2 = (-var_b + cmath.sqrt(disc)) / (2 * var_a)

        print("\nThe solutions of " + str(var_a) + "xˆ2 + " + str(var_b) + "x + " + str(var_c) + " are:\n")
        print("\tx1 = " + str(solution1))
        print("\tx2 = " + str(solution2))

    print("Thank you for using the Quadratic Solver App. Goodbye")

    return


if __name__ == '__main__':
    print("Welcome to the Quadratic Solver App.")
    print("\nA quadratic equation is of the form ax^2 + bx + c = 0\nYour solutions can be real or complex numbers.")
    print("A complex number has two parts: a + bj\nWhere a is a real portion and bj is the imaginary portion.")
    eq_num = int(input("\nHow many equations would you like to solve today: "))
    solve_equations(eq_num)