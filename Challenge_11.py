# CHALLENGE NUMBER 11
# TOPIC: For loop
# Binary hexadecimal conversion app
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060772#overview


def bin_hex_app(original_number):

    print("Generating lists....complete!")
    decimal_list = list(range(1, original_number + 1))
    print("\nUsing slices, we will nos show a portion of each list.")
    start_num = int(input("What decimal number would you like to start at: "))
    end_num = int(input("What decimal number would you like to stop at: "))

    print("\nDecimal values from " + str(start_num) + " to " + str(end_num))
    for num in decimal_list[start_num -1 :end_num]:
        print(num)

    print("\nBinary values from " + str(start_num) + " to " + str(end_num))
    for num in decimal_list[start_num - 1:end_num]:
        print(bin(num))

    print("\nHexadecimal values from " + str(start_num) + " to " + str(end_num))
    for num in decimal_list[start_num - 1:end_num]:
        print(hex(num))

    input(print("\nPress Enter to see all the values from 1 to " + str(original_number) + "."))
    print("Decimal----Binary----Hexadecimal\n------------------------------------------------------------------------")
    for num in decimal_list:
        print(str(num) + "----" + str(bin(num)) + "----" + str(hex(num)))

    return


if __name__ == '__main__':
    print("Welcome to the Binary/Hexadecimal Converter App")
    number = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
    bin_hex_app(number)