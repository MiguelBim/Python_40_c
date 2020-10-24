# CHALLENGE NUMBER 23
# TOPIC: Dic Struct
# Yes No Polling App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060822#overview


def yes_no_vote(question, num_of_voters, results_pwd):

    answers_dict = {}
    num_of_yes = 0
    num_of_no = 0

    for voter in range(num_of_voters):
        voter_name = input("\nEnter your full name: ").strip()
        if voter_name not in answers_dict.keys():
            print("Here is our issue: {}".format(question.title()))
            voter_answer = input("What do you think... yes or no: ").strip().lower()
            if voter_answer == 'yes' or voter_answer == 'y':
                num_of_yes += 1
                answers_dict[voter_name] = voter_answer
            elif voter_answer == 'no' or voter_answer == 'n':
                num_of_no += 1
                answers_dict[voter_name] = voter_answer
            else:
                answers_dict[voter_name] = voter_answer
                print("That is not a yes or no answer, but okay...")
            print("Thank you {}! Your vote of {} has been recorded.".format(voter_name.title(), voter_answer))
        else:
            print("Sorry, it seems that someone with that name has already voted")

    if len(answers_dict) > 0:
        print("\nThe following {} people voted:".format(len(answers_dict)))
        for key in answers_dict.keys():
            print("{}".format(key.title()))
        if num_of_yes > num_of_no:
            print("\nOn the following issue: {}".format(question))
            print("yes wins! {} vote(s) to {}.".format(num_of_yes, num_of_no))
        elif num_of_no > num_of_yes:
            print("\nOn the following issue: {}".format(question))
            print("no wins! {} vote(s) to {}.".format(num_of_no, num_of_yes))
        elif num_of_no == num_of_yes:
            print("\nOn the following issue: {}".format(question))
            print("It was a tie! {} vote(s) to {}.".format(num_of_no, num_of_yes))

        entry_pwd = input("\nTo see the voting results enter the admin password: ")
        if entry_pwd == results_pwd:
            for person, answer in answers_dict.items():
                print("Voter: {}\t\t\t\tVote: {}".format(person.title(), answer))
            print("\nThank you for using the Yes or No Issue Polling App.")
            return
        else:
            print("Incorrect password!")
    else:
        print("No one voted on this issue, exiting from app.")
        return


if __name__ == '__main__':
    print("Welcome to the Yes or No Issue Polling App")
    issue = input("\nWhat is the yes or no issue you will be voting on today: ").strip()
    num_of_voters = int(input("What is the number of voters you will allow on the issue: ").strip())
    results_pwd = input("Enter a password for polling results: ").strip()

    yes_no_vote(issue, num_of_voters, results_pwd)