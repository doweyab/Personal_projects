# Tic-Tac-Toe by Christian Thompson
# Using Loops & Functions & Lists

# STAGE I:
# Create the main loop
# Print the board
# Create your loop
# Get the user input
# Put the user input in the board

# STAGE II:
# Check for player win (8 Possibilities)

# STAGE III:
# Create the second player (NOT THE COMPUTER)
# Check for the second player win (8 Possibilities)
# Check for a full board (TIE)

# STAGE IV:
# Combine Stages II & III into 1 Function
# def is_winner(board, player):
# Create a function to check if the board is full
# def is_board_full(board)

# STAGE V:
# Creating our game AI
# def get_computer_move(board, player):
# i) Return random number
# ii) Make sure the random number is for an empty spot

# Import
import os
import time
import random

# Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


# Print the header
def print_header():
    print
    """
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    1 | 2 | 3
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      4 | 5 | 6
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     7 | 8 | 9
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\

 To play Tic-Tac-Toe, you need to get three in a row...
 Your choices are defined, they must be from 1 to 9...

"""


# Define the print_board function
def print_board():
    print
    "   |   |   "
    print
    " " + board[1] + " | " + board[2] + " | " + board[3] + "  "
    print
    "   |   |   "
    print
    "---|---|---"
    print
    "   |   |   "
    print
    " " + board[4] + " | " + board[5] + " | " + board[6] + "  "
    print
    "   |   |   "
    print
    "---|---|---"
    print
    "   |   |   "
    print
    " " + board[7] + " | " + board[8] + " | " + board[9] + "  "
    print
    "   |   |   "


def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False


def is_board_full(board):
    if " " in board:
        return False
    else:
        return True


def get_computer_move(board, player):
    # if the center square is empty choose that
    if board[5] == " ":
        return 5

    while True:
        move = random.randint(1, 9)
        # if the move is blank, go ahead and return, otherwise try again
        if board[move] == " ":
            return move
            break

    return 5


while True:
    os.system("clear")
    print_header()
    print_board()

    # Get Player X Input
    choice = input("Please choose an empty space for X. ")
    choice = int(choice)

    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print
        "Sorry, that space is not empty!"
        time.sleep(1)

    # Check for X win
    if is_winner(board, "X"):
        os.system("clear")
        print_header()
        print_board()
        print
        "X wins! Congratulations"
        break

    os.system("clear")
    print_header()
    print_board()

    # Check for a tie (is the board full)
    # If the board is full, do something
    if is_board_full(board):
        print
        "Tie!"
        break

    # Get Player O Input
    choice = get_computer_move(board, "O")

    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print
        "Sorry, that space is not empty!"
        time.sleep(1)

    # Check for O win
    if is_winner(board, "O"):
        os.system("clear")
        print_header()
        print_board()
        print
        "O wins! Congratulations"
        break

    # Check for a tie (is the board full)
    # If the board is full, do something
    if is_board_full(board):
        print
        "Tie!"
        break






