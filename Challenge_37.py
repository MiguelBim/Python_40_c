# CHALLENGE NUMBER 37
# TOPIC: Class
# Blackjack
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060916#overview


class Blackjack:

    def make_bet(self, user_money):
        print("\nCurrent money: ${}".format(user_money))
        user_bet = float(input("What would you like to  bet (minimum bet of 20): ").strip())
        print("\nCurrent Money: ${}\t\tCurrent Bet: ${}".format(user_money, user_bet))

    def play_game(self, bet_amount):
        return


def main():
    blackjack_game = Blackjack()
    print("Welcome to the Blackjack App.")
    print("The minimum bet at this table is $20.")
    user_money = float(input("\nHow much money are you willing to play with today: ").strip())
    blackjack_game.make_bet(user_money)


if __name__ == '__main__':
    main()