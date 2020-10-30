# CHALLENGE NUMBER 28
# TOPIC: While Struct
# Prime Number App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060854#overview

import time


def check_primer_num(number):

    if number > 1:
        for prev_num in range(2, number + 1):
            if prev_num == number:
                continue
            else:
                if number%prev_num == 0:
                    return print("{} is not prime!".format(number))
    else:
        print("{} is not prime!".format(number))

    return print("{} is prime!".format(number))


def display_primer_num(lower_bound, upper_bound):

    process_start_time = time.time()

    if lower_bound == 1:
        lower_bound = 2

    prime_numbers = []

    # while keep_looking:
    for num in range(lower_bound, upper_bound + 1):
        if num not in prime_numbers:
            flag = True
            for num_i in range(2, num + 1):
                if num_i == num:
                    continue
                else:
                    if num%num_i == 0:
                        flag = False
                        break
            if flag:
                prime_numbers.append(num)
            else:
                continue

    print("\nCalculations took a total of {} seconds.".format(round(time.time() - process_start_time, 4)))
    print("The following numbers between {} and {} are prime:".format(lower_bound, upper_bound))
    input("Press enter to continue:")
    for num in prime_numbers:
        print(num)

    return


if __name__ == '__main__':
    print("Welcome to the Prime Number App")

    run_app = True

    while run_app:
        print("\nEnter 1 to determine if a specific number is prime.")
        print("Enter 2 to determine all prime numbers within a set range")
        user_selection = int(input("Enter your choice 1 or 2: ").strip())

        if user_selection == 1:
            num = int(input("\nEnter a number tod determine if it is a prime or not: ").strip())
            check_primer_num(num)
        elif user_selection == 2:
            lower_limit = int(input("\nEnter the lower bound of your range: ").strip())
            upper_limit = int(input("Enter the upper bound of your range: ").strip())
            display_primer_num(lower_limit, upper_limit)
        else:
            print("\nThat is not a valid option")
        run_option = input("\nWould you like to run the program again (y/n): ").strip().lower()
        if run_option != 'y':
            print("\nThank you for using the program. Have a nice day.")
            run_app = False