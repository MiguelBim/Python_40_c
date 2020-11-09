# CHALLENGE NUMBER 34
# TOPIC: Funct
# Tic Tac Toe
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060898#overview


def display_base_template():

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("\tTic-Tac-Toe")
    for row in matrix:
        print("~"*17 + "\n||", end="")
        for num in row:
            print(" {} ||".format(num), end="")
        print("")
    print("~" * 17 + "\n")

    return


def display_current_template(matrix):

    print("\tTic-Tac-Toe")
    for row in matrix:
        print("~"*17 + "\n||", end="")
        for num in row:
            print(" {} ||".format(num), end="")
        print("")
    print("~" * 17 + "\n")

    return


def validate_win(matrix, sym):

    validation_matrix = [row[:] for row in matrix]

    for row in validation_matrix:
        for index, val in enumerate(row):
            if val != sym:
                row[index] = '_'

    win_options = [
        [[sym, sym, sym], ['_', '_', '_'], ['_', '_', '_']],
        [['_', '_', '_'], [sym, sym, sym], ['_', '_', '_']],
        [['_', '_', '_'], ['_', '_', '_'], [sym, sym, sym]],
        [[sym, '_', '_'], [sym, '_', '_'], [sym, '_', '_']],
        [['_', sym, '_'], ['_', sym, '_'], ['_', sym, '_']],
        [['_', '_', sym], ['_', '_', sym], ['_', '_', sym]],
        [[sym, '_', '_'], ['_', sym, '_'], ['_', '_', sym]],
        [['_', '_', sym], ['_', sym, '_'], [sym, '_', '_']],
    ]

    for option in win_options:
        if validation_matrix == option:
            return True
    return False


def validate_matrix(matrix):

    for row in matrix:
        for val in row:
            if val in '_':
                return True
    return False


def main():
    current_game_inputs = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    mapping_dict = {
        '1': [0, 0],
        '2': [0, 1],
        '3': [0, 2],
        '4': [1, 0],
        '5': [1, 1],
        '6': [1, 2],
        '7': [2, 0],
        '8': [2, 1],
        '9': [2, 2]
    }

    run_game = True
    while run_game:
        x_correct_ans = True
        o_correct_ans = True
        display_base_template()
        display_current_template(current_game_inputs)

        continue_running = validate_matrix(current_game_inputs)
        if not continue_running:
            print("\nThe matrix is completely filled up, it is a tie!")
            return

        while x_correct_ans:
            x_value = input("X: Where would you like to place your piece (1-9): ").strip()
            if int(x_value) <= 0 or int(x_value) > 9:
                print("That is not a spot on the board. Try again.")
            else:
                list_coordinates = mapping_dict[x_value]
                if current_game_inputs[list_coordinates[0]][list_coordinates[1]] != "_":
                    print("That spot has been chosen. Try again.")
                else:
                    current_game_inputs[list_coordinates[0]][list_coordinates[1]] = "X"
                    display_base_template()
                    display_current_template(current_game_inputs)
                    x_correct_ans = False
                    win_game = validate_win(current_game_inputs, "X")
                    if win_game:
                        print("Congratulations X, you win the game!")
                        return

        continue_running = validate_matrix(current_game_inputs)
        if not continue_running:
            print("\nThe matrix is completely filled up, it is a tie!")
            return

        while o_correct_ans:
            o_value = input("O: Where would you like to place your piece (1-9): ").strip()
            if int(o_value) <= 0 or int(o_value) > 9:
                print("That is not a spot on the board. Try again.")
            else:
                list_coordinates = mapping_dict[o_value]
                if current_game_inputs[list_coordinates[0]][list_coordinates[1]] != "_":
                    print("That spot has been chosen. Try again.")
                else:
                    current_game_inputs[list_coordinates[0]][list_coordinates[1]] = "O"
                    display_base_template()
                    display_current_template(current_game_inputs)
                    o_correct_ans = False
                    win_game = validate_win(current_game_inputs, "O")
                    if win_game:
                        print("Congratulations O, you win the game!")
                        return


if __name__ == '__main__':
    main()