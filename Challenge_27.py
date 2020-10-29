# CHALLENGE NUMBER 27
# TOPIC: While Struct
# Even Odd Sorter App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060850#overview


def even_odd_app(nums_chain):

    even_num = []
    odd_num = []
    nums_list = nums_chain.split(',')

    print("---- Result Summary -----")
    for i in range(len(nums_list)):
        nums_list[i] = nums_list[i].strip()
        if int(nums_list[i]) % 2 == 0:
            print("\t\t{} is even!".format(nums_list[i]))
            even_num.append(int(nums_list[i]))
        else:
            print("\t\t{} is odd!".format(nums_list[i]))
            odd_num.append(int(nums_list[i]))

    print("\nThe following 5 numbers are even:")
    for num in sorted(even_num):
        print("\t\t{}".format(num))

    print("\nThe following 5 numbers are odd:")
    for num in sorted(odd_num):
        print("\t\t{}".format(num))

    return


if __name__ == '__main__':

    #1, 2, 3, 6,18,9,4,13,22
    #5,1, 66, 23, 5, 234, 6
    print("Welcome to the Even Odd Number sorter App")
    run = True
    while run:
        nums_chain = input("\nEnter in a string of numbers separated by a comma (,) : ")
        even_odd_app(nums_chain)
        run_again = input("\nWould you like to run the program again (y/n): ").lower().strip()
        if run_again != 'y':
            print("Thank you for using the program. Goodbye.")
            run = False