# CHALLENGE NUMBER 10
# TOPIC: Lists
# Basketball Favorites teacher program.
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060760#overview

def favorite_teacher():

    teachers_list = []
    print("Welcome to the Favorite Teachers Program\n")
    first_teacher = input("Who is your first favorite teacher: ").title()
    teachers_list.append(first_teacher)
    second_teacher = input("Who is your second favorite teacher: ").title()
    teachers_list.append(second_teacher)
    third_teacher = input("Who is your third favorite teacher: ").title()
    teachers_list.append(third_teacher)
    fourth_teacher = input("Who is your fourth favorite teacher: ").title()
    teachers_list.append(fourth_teacher)

    ordered_teachers_list = sorted(teachers_list)
    print("\nYour favorite teachers ranked are: " + str(teachers_list))
    print("Your favorite teachers alphabetically are: " + str(ordered_teachers_list))
    ordered_teachers_list.sort(reverse=True)
    print("Your favorite teachers in reverse alphabetically order are: " + str(ordered_teachers_list))
    print("\nYour top two teachers are: " + str(teachers_list[0]) + " and " + str(teachers_list[1]))
    print("Your next two favorite teachers are: " + str(teachers_list[2]) + " and " + str(teachers_list[3]))
    print("Your last favorite teacher is: " + str(teachers_list[-1]))
    print("You have a total of 4 favorite teachers.")
    new_teacher = input("\nOops, " + str(teachers_list[0]) + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ")

    teachers_list.insert(0, new_teacher.title())
    ordered_teachers_list = sorted(teachers_list)
    print("\nYour favorite teachers ranked are: " + str(teachers_list))
    print("Your favorite teachers alphabetically are: " + str(ordered_teachers_list))
    ordered_teachers_list.sort(reverse=True)
    print("Your favorite teachers in reverse alphabetically order are: " + str(ordered_teachers_list))
    print("\nYour top two teachers are: " + str(teachers_list[0]) + " and " + str(teachers_list[1]))
    print("Your next two favorite teachers are: " + str(teachers_list[2]) + " and " + str(teachers_list[3]))
    print("Your last favorite teacher is: " + str(teachers_list[-1]))
    print("You have a total of 5 favorite teachers.")

    removed_teacher = input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title()
    teachers_list.remove(removed_teacher)
    ordered_teachers_list = sorted(teachers_list)
    print("\nYour favorite teachers ranked are: " + str(teachers_list))
    print("Your favorite teachers alphabetically are: " + str(ordered_teachers_list))
    ordered_teachers_list.sort(reverse=True)
    print("Your favorite teachers in reverse alphabetically order are: " + str(ordered_teachers_list))
    print("\nYour top two teachers are: " + str(teachers_list[0]) + " and " + str(teachers_list[1]))
    print("Your next two favorite teachers are: " + str(teachers_list[2]) + " and " + str(teachers_list[3]))
    print("Your last favorite teacher is: " + str(teachers_list[-1]))
    print("You have a total of 4 favorite teachers.")

    return


if __name__ == '__main__':
    favorite_teacher()