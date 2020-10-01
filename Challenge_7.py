# CHALLENGE NUMBER 7
# TOPIC: Lists
# Sorting List
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060738#overview


def sort_lists():

    num_strings = ['15', '100', '55', '42']
    num_ints = [15, 100, 55, 42]
    num_floats = [2.2, 5.0, 1.245, 0.142857]
    num_lists = [[1,2,3], [4,5,6], [7,8,9]]

    print("\t\tSummary Table")

    print("The variable num_strings is a " + str(type(num_strings)))
    print("It contains the elements: " + str(num_strings))
    print("The element " + num_strings[0] + " is a " + str(type(num_strings[0])) + ".")

    print("\nThe variable num_ints is a " + str(type(num_ints)))
    print("It contains the elements: " + str(num_ints))
    print("The element " + str(num_ints[0]) + " is a " + str(type(num_ints[0])) + ".")

    print("\nThe variable num_floats is a " + str(type(num_floats)))
    print("It contains the elements: " + str(num_floats))
    print("The element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])) + ".")

    print("\nThe variable num_lists is a " + str(type(num_lists)))
    print("It contains the elements: " + str(num_lists))
    print("The element " + str(num_lists[0]) + " is a " + str(type(num_lists[0])) + ".")

    num_strings.sort()
    num_ints.sort()
    print("\nNow sorting num_strings and num_ints...")
    print("Sorted num_strings: " + str(num_strings))
    print("Sorted num_ints: " + str(num_ints))
    print("\nStrings are sorted alphabetically while integers are sorted numerically!")

    return


if __name__ == '__main__':
    sort_lists()