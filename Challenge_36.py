# CHALLENGE NUMBER 36
# TOPIC: Class
# Pythonoganchi
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060912#overview
import random


class Creature:

    def __init__(self, name):
        self.name = name

    def feed_creature(self, name, features, food_available, difficult_level):
        if food_available <= 0:
            print("Sorry, there is no food available. {} is dead".format(name))
            return False, 0
        else:
            eaten_food = random.randint(1, food_available)
            increase_val = random.randint(1, 10 - difficult_level)
            features['hunger'] -= increase_val
            print("Yum! {} has eaten {} portions.".format(name, eaten_food))
            tired_increase = random.randint(1, difficult_level)
            dirty_increase = random.randint(1, difficult_level)
            features['tiredness'] += tired_increase
            features['dirtiness'] += dirty_increase
        return True, eaten_food

    def play_with_creature(self):
        return

    def sleep_creature(self):
        return

    def take_a_bath(self):
        return


def display_creature_status(name, creature_dict, food, status):
    print("\nCreature Name: {}".format(name))
    for action, value in creature_dict.items():
        print("{} (0-10): {}".format(action.title(), value))
    print("\nFood Inventory: {} pieces".format(food))
    print("Current Status: {}".format(status))


def action_to_do():

    print("Enter (1) to eat.")
    print("Enter (2) to play.")
    print("Enter (3) to sleep.")
    print("Enter (4) to take a bath.")
    print("Enter (5) to forage for food.")
    choice = int(input("What is your choice: ").strip())

    return choice


def main():
    print("Welcome to the Pythonogachi Simulator App")
    round_counter = 1
    play_game = True
    game_difficulty = int(input("Please choose a difficulty level (1-5): ").strip())
    if game_difficulty <= 0 or game_difficulty > 5:
        print("Sorry, that value is not correct. Please try again")
    else:
        creature_name = input("What name would you like to give your pet Pythonogachi: ").strip().title()
        current_status = 'Awake'
        live = True
        creature_features = {'hunger': 0, 'boredom': 0, 'tiredness': 0, 'dirtiness': 0}
        food_inventory = random.randint(1, 10 - game_difficulty)

        creature = Creature(creature_name)

        print()
        while play_game:
            print("\n" + "-"*50 + "\nRound #{}".format(round_counter))
            display_creature_status(creature_name, creature_features, food_inventory, current_status)
            action = action_to_do()
            if action == 1:
                live, food_consumed = creature.feed_creature(creature_name, creature_features, food_inventory, game_difficulty)
                food_inventory -= food_consumed
                print("\nRound #{} Summary: ".format(round_counter))
                display_creature_status(creature_name, creature_features, food_inventory, current_status)

            if not live:
                play_game = False
                return
            else:
                round_counter += 1
    return


if __name__ == '__main__':
    main()