# CHALLENGE NUMBER 6
# TOPIC: Lists
# Grade Sorter Appa
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060734#overview

# NOTES

def grade_app(grades_list):

    print("\nYour grades are: " + str(grades_list))
    grades_list.sort(reverse=True)
    print("\nYour grades from highest to lowest are: " + str(grades_list))
    print("\nThe two lowest grades will now be dropped.")
    lowest_grade = grades_list.pop()
    second_lowest_grade = grades_list.pop()
    print("Removed grade: " + str(lowest_grade))
    print("Removed grade: " + str(second_lowest_grade))
    print("\nYour remaining grades are: " + str(grades_list))
    print("Nice work! Your highest grade is a " + str(grades_list[0]) + ".")

    return


if __name__ == '__main__':

    grades = []
    print("Welcome to the Grade Sorter App\n")
    grades.append(int(input("What is your first grade (0-100): ")))
    grades.append(int(input("What is your second grade (0-100): ")))
    grades.append(int(input("What is your third grade (0-100): ")))
    grades.append(int(input("What is your fourth grade (0-100): ")))
    grade_app(grades)