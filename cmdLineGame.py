# A Command Line dynamic TIC TAC TOE GAME.
# Requirements:- Python3.
# TIC TAC TOE Board is dynamic can be of any size.
# 2 Player game Player1 will choose 'X' position and Player2 will choose 'O' position on the game board.
# A winner s chosen if all the input('X'/'O') in a row/column/diagonal are same.
# Program gives the Winner/No winner.
# Once the game finishes, user are asked to play again or want to quit.


from colorama import Fore, Back, Style, init
import os
import time
init()


# Defining a clear function to make our game screen clean.
def clear():
    os.system('cls')


# Function to draw our game board based on user input
def game(game_map, player, row, col, cr):
    try:
        # Checking if user input position is already taken
        if game_map[row][col] != 0:
            print("This position is already occupied, Choose another!!")
            print()
            return False
        clear()

        # printing the column values on the gameboard
        print("   "+"  ".join([str(x) for x in range(len(game_map))]))
        if player != 0:
            game_map[row][col] = player

        # enumerate function is used to print row indexes
        # replacing all 0 to "", 1 to 'X' and 2 to '0'
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)
        print()
        return game_map
    # handling Out of range error
    except IndexError as e:
        print("Error: Did you enter row/column as ({})?".format(cr), e)
        print()
        return False
    # handling input type error
    except TypeError as e:
        print("Error: Did you pass the correct parameters for list:", e)
        print()
        return False


# function to decide winner
def win(current_game):
    # Horizontal Winner
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    for row in current_game:
        if all_same(row):
            print("Player {} is the winner horizontally!".format(row[0]))
            return True

    # Vertical Winner
    column = range(len(current_game))
    for col in column:
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print("Player {} is the winner vertically!".format(check[0]))
            return True

    # Diagonal Winner Type1 ((0,2), (1,1), (2,0))
    diags1 = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags1.append(current_game[row][col])
    if all_same(diags1):
        print("Player {} is the winner diagonally!".format(diags1[0]))
        return True

    # Diagonal Winner Type2 ((0,0), (1,1), (2,2))
    diags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally!")
        return True
    return False


# main loop
play = True
while play:
    players = [1, 0]
    # p = [1,2]
    game_size = int(input("Enter the tic_tac_toe game size:"))
    game_boards = [[0 for i in range(game_size)] for i in range(game_size)]
    choice_range = ", ".join([str(i) for i in range(game_size)])
    game_won = False
    game(game_boards, 0, 0, 0, choice_range)
    choice = 0
    total_turn_possible = game_size * game_size
    while not game_won:
        if total_turn_possible >=1:
            current_player = choice + 1
            played = False
            while not played:
                time.sleep(.5)
                print("Current_Player:", current_player)
                # Collecting the row and column choices of current player
                row_choice = int(input(f"Which row do you want to choose player{current_player}? choice range - ({choice_range}):"))
                column_choice = int(input(f"Which column do you want to choose player{current_player}? choice range - ({choice_range}):"))
                g = game(game_boards, current_player, row_choice, column_choice, choice_range)
                if g:
                    played = True

            # Checking for any winner
            game_won = win(g)

            # reversing the turn between player1 and player2
            choice = players[choice]
        else:
            game_won = True
            print("No Winners!!!")
        total_turn_possible -= 1

    # Asking if  user want to replay...
    replay = input("press 'N' to quit or any other key to continue:")
    if replay == 'N' or replay == 'n':
        print("Bye!!!")
        play = False
    else:
        print()
        print("_________restarting_________")
        print()
