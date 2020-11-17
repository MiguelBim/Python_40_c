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
            return 0, False
        else:
            eaten_food = random.randint(1, food_available)
            increase_val = random.randint(1, 10 - difficult_level)
            features['hunger'] -= increase_val
            print("\nYum! {} has eaten {} portions.".format(name, eaten_food))
            tired_increase = random.randint(1, difficult_level)
            dirty_increase = random.randint(1, difficult_level)
            features['tiredness'] += tired_increase
            features['dirtiness'] += dirty_increase
            if features['tiredness'] > 10:
                print("\n{} was so bored, you did not play with it. Now it is dead!".format(name))
                return eaten_food, False
            elif features['dirtiness'] > 10:
                print("\n{} needed a bath! Now it has dead!".format(name))
                return eaten_food, False
        return eaten_food, True

    def play_with_creature(self, name, features, difficult_level):

        decrease_val = random.randint(1, 10 - difficult_level)
        features['boredom'] -= decrease_val
        print("\n{} wants to play a game.".format(name))
        pet_number = random.randint(1, 3)
        print("{} is thinking of a number 0, 1 or 2.".format(name))
        user_guess = int(input("What is your guess: ").strip())
        if user_guess == pet_number:
            print("Correct, you guessed the number")
        else:
            print("Wrong! {} was thinking of {}".format(name, pet_number))
        tired_increase = random.randint(1, difficult_level)
        dirty_increase = random.randint(1, difficult_level)
        hunger_increase = random.randint(1, difficult_level)
        features['tiredness'] += tired_increase
        features['dirtiness'] += dirty_increase
        features['hunger'] += hunger_increase
        if features['hunger'] > 10:
            print("\nYou forgot to feed {}, no it is dead! ".format(name))
            return False
        elif features['tiredness'] > 10:
            print("\n{} was so bored, you did not play with it. Now it is dead!".format(name))
            return False
        elif features['dirtiness'] > 10:
            print("\n{} needed a bath! Now it has dead!".format(name))
            return False
        return True

    def sleep_creature(self, name, features, difficult_level):

        decrease_val = random.randint(1, 10 - difficult_level)
        features['tiredness'] -= decrease_val
        print("{} is sleepy. Falling asleep!".format(name))
        hunger_increase = random.randint(1, difficult_level)
        features['hunger'] += hunger_increase
        sleeping = True
        if features['hunger'] > 10:
            print("\nYou forgot to feed {}, no it is dead! ".format(name))
            return sleeping, False
        return sleeping, True

    def take_a_bath(self, name, features, difficult_level):

        decrease_val = random.randint(1, 10 - difficult_level)
        features['dirtiness'] -= decrease_val
        print("{} has taken a bath. All clean!".format(name))
        tired_increase = random.randint(1, difficult_level)
        hunger_increase = random.randint(1, difficult_level)
        features['tiredness'] += tired_increase
        features['hunger'] += hunger_increase
        if features['hunger'] > 10:
            print("\nYou forgot to feed {}, no it is dead! ".format(name))
            return False
        elif features['tiredness'] > 10:
            print("\n{} was so bored, you did not play with it. Now it is dead!".format(name))
            return False
        return True

    def forage_food(self, name, features, difficult_level):

        food_found = random.randint(1, 10 - difficult_level)
        print("{} found {} pieces of food!".format(name, food_found))
        hunger_increase = random.randint(1, difficult_level)
        tired_increase = random.randint(1, difficult_level)
        features['hunger'] += hunger_increase
        features['tiredness'] += tired_increase
        sleeping = True
        if features['hunger'] > 10:
            print("\nYou forgot to feed {}, no it is dead! ".format(name))
            return food_found, False
        elif features['tiredness'] > 10:
            print("\n{} was so bored, you did not play with it. Now it is dead!".format(name))
            return food_found, False
        return food_found, True


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
        sleep = False
        creature_features = {'hunger': 0, 'boredom': 0, 'tiredness': 0, 'dirtiness': 0}
        food_inventory = random.randint(1, 10 - game_difficulty)

        creature = Creature(creature_name)

        print()
        while play_game:
            print("\n" + "-"*50 + "\nRound #{}".format(round_counter))
            display_creature_status(creature_name, creature_features, food_inventory, current_status)
            action = action_to_do()
            if action == 1:
                food_consumed, live = creature.feed_creature(creature_name, creature_features, food_inventory, game_difficulty)
                food_inventory -= food_consumed
            elif action == 2:
                live = creature.play_with_creature(creature_name, creature_features, game_difficulty)
            elif action == 3:
                sleep, live = creature.sleep_creature(creature_name, creature_features, game_difficulty)
            elif action == 4:
                live = creature.take_a_bath(creature_name, creature_features, game_difficulty)
            elif action == 5:
                new_food, live = creature.forage_food(creature_name, creature_features, game_difficulty)
                food_inventory += new_food

            while sleep:
                awake = int(input("\nEnter (6) to try to wake up: ").strip())
                if awake == 6:
                    print("{} just woke up".format(creature_name))
                    sleep = False
                else:
                    print("Upps, that did not worked. {} is still sleeping".format(creature_name))
            print("\nRound #{} Summary: ".format(round_counter))
            display_creature_status(creature_name, creature_features, food_inventory, current_status)

            if not live:
                play_game = False
            else:
                round_counter += 1
    return


if __name__ == '__main__':
    main()