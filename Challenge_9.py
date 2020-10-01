# CHALLENGE NUMBER 9
# TOPIC: Lists
# Basketball Roster Program.
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060748#overview

import random as rd

def basketball_roster():

    print("Welcome to the Bastekball Roster Program\n")
    list_players = []
    list_players.append(input("Who is your point guard: "))
    list_players.append(input("Who is your shooting guard: "))
    list_players.append(input("Who is your small forward: "))
    list_players.append(input("Who is your power forward: "))
    list_players.append(input("Who is your center: "))

    print("\n\tYou are starting 5 for the upcoming basketball season")
    print("\t\tPoint Guard:\t\t" + list_players[0].title())
    print("\t\tShooting Guard:\t\t" + list_players[1].title())
    print("\t\tSmall Forward:\t\t" + list_players[2].title())
    print("\t\tPower Forward:\t\t" + list_players[3].title())
    print("\t\tCenter:\t\t\t\t" + list_players[4].title())

    random_number = rd.randrange(len(list_players))
    new_player = input("\nOh no, " + list_players[random_number].title() + " is injured.\nYour roster only has 4 players.\nWho will take " + list_players[random_number].title() + "'s spot: ")
    list_players[random_number] = new_player

    print("\n\tYou are starting 5 for the upcoming basketball season")
    print("\t\tPoint Guard:\t\t" + list_players[0].title())
    print("\t\tShooting Guard:\t\t" + list_players[1].title())
    print("\t\tSmall Forward:\t\t" + list_players[2].title())
    print("\t\tPower Forward:\t\t" + list_players[3].title())
    print("\t\tCenter:\t\t" + list_players[4].title())
    print("\nGood luck " + list_players[random_number].title() + " you will do great!\nYour roster now has 5 players")

    return


if __name__ == '__main__':
    basketball_roster()
