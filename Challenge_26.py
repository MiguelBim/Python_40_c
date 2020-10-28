# CHALLENGE NUMBER 26
# TOPIC: While Struct
# Factor Generator App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060842#overview


def factor_generator(original_number):

    print("Factors of {} are: ".format(original_number))
    counter = 1
    factors_list = []
    while counter <= original_number:
        if original_number%counter == 0:
            factors_list.append(counter)
            print(counter)
        counter += 1

    print("\nIn summary:")
    if len(factors_list) % 2 != 0:
        num_list_limit = int((len(factors_list) - 1) / 2)
    else:
        num_list_limit = int((len(factors_list)) / 2)
    for i in range(num_list_limit):
        print("{} * {} = {}".format(factors_list.pop(0), factors_list.pop(), original_number))

    return


if __name__ == '__main__':

    print("Welcome to the Factor Generator App")
    run_program = True
    while run_program:
        entry_num = int(input("\nEnter a number to determine all factors of that number: ").strip())
        factor_generator(entry_num)
        run_again = input("\nRun again (y/n): ").lower().strip()
        if run_again != "y":
            print("Thank you for using the program. Have a great day.")
            run_program = False
