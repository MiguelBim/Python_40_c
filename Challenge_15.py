# CHALLENGE NUMBER 15
# TOPIC: For loop
# Factorial Calculator App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060788#overview


def calculate_gpa(name, grades_list):

    grades_list.sort(reverse=True)
    copy_original_list = grades_list.copy()
    grades_sum = sum(grades_list)
    avg_grade = grades_sum/len(grades_list)
    print("\nGrades Highest to Lowers")
    for grade in grades_list:
        print("\t\t" + str(grade))

    print("\nMike's Grade Summary:")
    print("\t\tTotal Number of Grades: " + str(len(grades_list)))
    print("\t\tHighest Grade: " + str(grades_list[0]))
    print("\t\tLowest Grade: " + str(grades_list[-1]))
    print("\t\tAverage: " + str(avg_grade))

    des_average = float(input("\n What is your desired average: "))
    needed_score = ((len(grades_list) + 1) * des_average) - grades_sum
    print("\nGood luck " + str(name.title()) + "!")
    print("You will need to get a " + str(needed_score) + " on your next assignment to earn a " + str(des_average) + " average.")

    print("\nLets see what your average could have been if you did better/worse on an assignment.")
    grade_to_change = int(input("What grade would you like to change: "))
    new_grade = int(input("What grade would you like to change " + str(grade_to_change) + " to: "))

    for index, val in enumerate(grades_list):
        try:
            if val == grade_to_change:
                grades_list[index] = new_grade
                break
            else:
                continue
        except:
            print("That value is not on the list")
            break

    new_grades_sum = sum(grades_list)
    new_avg_grade = new_grades_sum/len(grades_list)

    grades_list.sort(reverse=True)
    print("\nNew Grades Highest to Lowest:")
    for grade in grades_list:
        print("\t\t" + str(grade))

    print("\nMike's New Grade Summary:")
    print("\t\tTotal Number of Grades: " + str(len(grades_list)))
    print("\t\tHighest Grade: " + str(grades_list[0]))
    print("\t\tLowest Grade: " + str(grades_list[-1]))
    print("\t\tAverage: " + str(new_avg_grade))

    print("\nYour new average would be a " + str(new_avg_grade) + " compared to your real average of " + str(avg_grade) + "!")
    print("This is a change of " + str(round(new_avg_grade - avg_grade, 2)) + " points!")
    print("\nToo bad your original grades are still the same!")
    print(copy_original_list)
    print("You should go ask for extra credit")

    return


if __name__ == '__main__':
    print("Welcome to the Average Calculator App")
    name = input("\nWhat is your name: ")
    num_of_grades = int(input("How many grades would you like to enter: "))

    grades_list = []
    for i in range(num_of_grades):
        grade = int(input("Enter grade: "))
        grades_list.append(grade)

    calculate_gpa(name, grades_list)