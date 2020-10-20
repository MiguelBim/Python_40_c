# CHALLENGE NUMBER 18
# TOPIC: Conditional
# Voter Registration App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060802#overview


def voter_registration(name):

    political_parties_list = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
    print("\nHere is a list of political parties to join.")
    for party in political_parties_list:
        print("\t- {}".format(party))

    party_election = input("\nWhat party would you like to join: ").title().strip()

    if party_election in political_parties_list:
        print("\nCongratulations {}! You have joined the {} party!".format(name, party_election))

        if party == "Republican" or "Democratic":
            print("That is a major party.")
        elif party == "Independent":
            print("You are an Independent Person!")
        else:
            print("That is not a major party.")
    else:
        print("\nSorry, {} is not a Political Party. Please check!".format(party_election))

    return


if __name__ == '__main__':
    print("Welcome to the Voter Registration App")
    applicant_name = input("\nPlease enter your name: ").title().strip()
    applicant_age = int(input("Please enter your age: "))

    if applicant_age >= 18:
        print("\nCongratulations {}! You are old enough to register to vote.".format(applicant_name))
        voter_registration(applicant_name)
    else:
        print("\nYou are not old enough to register to vote.")