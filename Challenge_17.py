# CHALLENGE NUMBER 17
# TOPIC: Conditional
# Coin Toss App
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17151710#overview

import random


def coin_toss_app(num_of_flips, watch_results):

    heads_count = 0
    tails_count = 0

    for flip in range(num_of_flips):
        result = random.randrange(1,3)
        if result == 1:
            heads_count += 1
            if watch_results == 'y':
                print("HEADS")
        if result == 2:
            tails_count += 1
            if watch_results == 'y':
                print("TAILS")

    heads_perc = round((float(heads_count) * 100) / num_of_flips, 2)
    tails_perc = round((float(tails_count) * 100) / num_of_flips, 2)

    print("\nResults Of Flipping A Coin {} Times:\n".format(num_of_flips))
    print("Side\t\tCount\t\tPercentage")
    print("Heads\t\t{}/{}\t\t\t{}%".format(heads_count, num_of_flips, heads_perc))
    print("Tails\t\t{}/{}\t\t\t{}%".format(tails_count, num_of_flips, tails_perc))

    return


if __name__ == '__main__':
    print("Welcome to the Coin Toss App")
    print("\nI will flip a coin a set number of times.")
    num_of_flips = int(input("How many times would you like me to flip the coin: "))
    watch_results = input("Would you like to see the result of each flip (y/n): ").lower().strip()
    coin_toss_app(num_of_flips, watch_results)