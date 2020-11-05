# CHALLENGE NUMBER 32
# TOPIC: Funct
# Calculator App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060880#overview


def sum_operation(num_1, num_2):
    return print("The sum of {} and {} is {}.".format(num_1, num_2, num_1 + num_2))


def sub_operation(num_1, num_2):
    return print("The subtraction of {} and {} is {}.".format(num_1, num_2, num_1 - num_2))


def mult_operation(num_1, num_2):
    return print("The product of {} and {} is {}.".format(num_1, num_2, num_1 * num_2))


def div_operation(num_1, num_2):
    return print("The division of {} and {} is {}.".format(num_1, num_2, num_1 / num_2))


def exp_operation(num_1, num_2):
    return print("The exponent of {} and {} is {}.".format(num_1, num_2, num_1 ** num_2))


if __name__ == '__main__':
    print("Welcome to the Python Calculator App")
    print("Enter two numbers and an operation and the desired operation will be performed")

    run_program = True
    while run_program:
        number_one = float(input("\nEnter a number: ").strip())
        number_two = float(input("Enter a number: ").strip())
        operation = input("Enter an operation (addition, subtraction, multiplication, division or exponentiation): ").strip().lower()
        if operation == 'addition':
            sum_operation(number_one, number_two)
        elif operation == 'subtraction':
            sub_operation(number_one, number_two)
        elif operation == 'multiplication':
            mult_operation(number_one, number_two)
        elif operation == 'division':
            if number_two != 0:
                div_operation(number_one, number_two)
            else:
                print("You can not divide by 0")
        elif operation == 'exponentiation':
            exp_operation(number_one, number_two)
        else:
            print("This is not a valid operation. Try again")
        continue_running = input("Would you like to run the program again (y/n): ").strip().lower()
        if continue_running != 'y':
            run_program = False
            print("Thank you for using this app.")