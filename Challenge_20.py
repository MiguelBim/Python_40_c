# CHALLENGE NUMBER 20
# TOPIC: Conditional
# Rock, Paper, Scissors
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060812#overview

import random


def play_rps_game(num_of_rounds):

    player_score = 0
    computer_score = 0
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    option_inv = {'rock': 1, 'paper': 2, 'scissors': 3}

    for round_num in range(1, num_of_rounds + 1):
        print("\nRound {}".format(round_num))
        print("Player: {}\t Computer: {}".format(player_score, computer_score))
        player_entry = input("Time to pick...rock, paper, scissors: ").lower().strip()
        try:
            player_election = option_inv[player_entry]
        except:
            player_election = -1
        computer_election = random.randint(1,3)
        print("\tComputer: {}".format(options[computer_election]))
        print("\tPlayer: {}".format(player_entry))
        if player_election == computer_election:
            print("\tIt is a tie, how boring!")
            print("\tThis round was a tie.")
        elif player_election == 1 and computer_election == 2:
            print("\tPaper covers rock!")
            print("\tComputer wins round {}.".format(round_num))
            computer_score += 1
        elif player_election == 1 and computer_election == 3:
            print("\tRock crashes scissors!")
            print("\tYou win round {}.".format(round_num))
            player_score += 1
        elif player_election == 2 and computer_election == 1:
            print("\tPaper covers rock!")
            print("\tYou win round {}.".format(round_num))
            player_score += 1
        elif player_election == 2 and computer_election == 3:
            print("\tScissors cuts paper!")
            print("\tComputer wins round {}.".format(round_num))
            computer_score += 1
        elif player_election == 3 and computer_election == 1:
            print("\tRock crashes scissors!")
            print("\tComputer wins round {}.".format(round_num))
            computer_score += 1
        elif player_election == 3 and computer_election == 2:
            print("\tScissors cuts paper!")
            print("\tYou win round {}.".format(round_num))
            player_score += 1
        else:
            print("\tThis is not a valid game option!")
            print("\tComputer gets the point")
            computer_score += 1

    print("\nFinal Game Results")
    print("\tRounds Played: {}".format(num_of_rounds))
    print("\tPlayer Score: {}".format(player_score))
    print("\tComputer Score: {}".format(computer_score))
    if player_score > computer_score:
        print("\tWinner: Player :-)")
    elif player_score < computer_score:
        print("\tWinner: Computer :-(")
    else:
        print("\tWinner: It is a tie :-|")

    return


if __name__ == '__main__':
    print("Welcome to a game of Rock, Paper, Scissors")
    num_of_rounds = int(input("\nHow many rounds would you like to play: ").strip())
    play_rps_game(num_of_rounds)