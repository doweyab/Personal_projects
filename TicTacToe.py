import calendar
from datetime import date
import time
import sys
import random


class Game:

    def __init__(self, players):
        """
        This method used initialisation game with players and load the game board
        :param players:
        """
        self.players = players
        self.board = Board()

    def play_game(self):
        """
        Game will start from here each player will turn accordingly
        empty board will print initially but each turn of player
        Board class method will check the player status either it be a draw or win
        after that board will print again until game is over
        :return:
        """
        while True:

            for player in self.players:
                print(self.board)
                print("Your turn player {}".format(player))

                self.play_turn_for_player(player)

                if self.board.is_draw():
                    print("Its a draw!")
                    return "draw"

                elif self.board.is_victory(player.icon):
                    print(self.board)
                    print("{} Wins! Congrats!".format(player.icon))
                    return player.name

    def play_turn_for_player(self, player):
        """
         This method is responsible for each player turn
         first it call Player class method to get a valid move
         and then use Board class to assign this move to game
         board with respect to player
        :param player:
        """
        while True:
            try:
                move = player.get_move(self.board)
                self.board.player_move(move, player.icon)
                break

            except InvalidChoiceError:
                continue

class Player:

    """
    Player class initialize player with their icon and name
    """

    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    def __str__(self):
        return self.icon

class Human(Player):

    """
    This will initialize the human player on start system take input for player name,
    Human class have get move method which will take input from player in range of 1-9 according to the game board
    and also check is it valid choice or not
    """

    def __init__(self, icon):
        super().__init__(icon, name=input("Whats your name? "))

    def get_move(self, board):

        while True:
            try:
                choice = int(input("Enter your move (1-9): "))
                if choice not in range(1, 10):
                    raise NotABoxNumberError
                return choice - 1

            except ValueError:
                print("Enter a valid box number")
            except NotABoxNumberError:
                print("Enter a valid box number from 1 to 9 please!")

class EasyAi(Player):

    """
    EasyAi just get the empty spaces on board, after that it attempt a random number from 1-9
    and if it's in the board available space or empty space then mark this cell with the respective icon
    """

    def __init__(self, icon):
        super().__init__(icon, "EasyAi")

    def get_move(self, board):
        spaces = board.get_open_spaces()

        while True:
            attempt = random.randint(1, 9)
            if attempt in spaces:
                return attempt

class HarderAi(Player):

    """
    HarderAi have a bit more intelligent 'get_move' method

    At first loop it get all the spaces available on the board after that it iterate over these
    spaces on each iteration it create the copy of current game board and assign the move to
    the copied board and check it's state, is it victory or not, if it's victory then assign this move
    to original board

    At second loop it does the same thing but for other player and get his/her potential win move and
    assign this move to original player to restrict him/her

    If there is no win available and the center cell/move is available/empty return that

    if center move not available then system try to choose from following option
    0 : first move of first row
    2 : center move of first row
    6 : last move of second row
    8 : center move of third row

    if above mention moves are also not available then it simply behave like EasyAi
    """

    def __init__(self, icon):
        super().__init__(icon, "HarderAi")

    def get_move(self, board):

        spaces = board.get_open_spaces()

        for move in spaces:
            board_copy = board.copy_board()
            board_copy.player_move(move, self.icon)
            if board_copy.is_victory(self.icon):
                return move

        for move in spaces:
            board_copy = board.copy_board()
            board_copy.player_move(move, flip_icon(self.icon))
            if board_copy.is_victory(flip_icon(self.icon)):
                return move

        # taking a center move if no possible wins
        if 5 in spaces:
            return 5
        for move in [0, 2, 6, 8]:
            if move in spaces:
                return move

        while True:
            attempt = random.randint(1, 9)
            if attempt in spaces:
                return attempt

class Board:

    """
    Load the board with Nine empty cells
    """

    def __init__(self):
        self.board = [" " for i in range(9)]

    """
    Return the game board state
    """

    def __str__(self):
        row_1 = " {} | {} | {} ".format(self.board[0], self.board[1], self.board[2])
        row_2 = " {} | {} | {} ".format(self.board[3], self.board[4], self.board[5])
        row_3 = " {} | {} | {} ".format(self.board[6], self.board[7], self.board[8])
        full_rows = "\n{}\n{}\n{}\n".format(row_1, row_2, row_3)
        return full_rows

    """
    Player movement method and assign the cell to respective icon if possible
    """

    def player_move(self, move, icon):

        if self.board[move] == " ":
            self.board[move] = icon
        else:
            print("That space is taken!")
            raise InvalidChoiceError

    """
    Check if any row is in win state for respective player
    """

    def row_contains_win(self, icon):
        for row_number in range(3):
            if self.board[0 + 3 * row_number] == icon and \
                    self.board[1 + 3 * row_number] == icon and \
                    self.board[2 + 3 * row_number] == icon:
                return True
        return False

    """
    Check if any column is in win state for respective player
    """

    def column_contains_win(self, icon):
        for column_number in range(3):
            if self.board[column_number] == icon and \
                    self.board[column_number + 3] == icon and \
                    self.board[column_number + 6] == icon:
                return True
        return False

    """
    Check if any diagonal is in win state for respective player
    """

    def diagonal_contains_win(self, icon):
        return (self.board[0] == icon and self.board[4] == icon and self.board[8] == icon) \
               or (self.board[2] == icon and self.board[4] == icon and self.board[6] == icon)

    """
    This method call it's child method to check the respective player state is it a win or not
    """

    def is_victory(self, icon):
        return self.row_contains_win(icon) or \
               self.column_contains_win(icon) or \
               self.diagonal_contains_win(icon)

    """
    This method check if it draw like If all the cells are marked and either of player not in win state game will draw
    """

    def is_draw(self):
        return " " not in self.board

    """
    Return the available options of game board or empty cells
    """

    def get_open_spaces(self):
        spaces = []
        for i in range(0, 9):
            if " " in self.board[i]:
                spaces += [i]
        return spaces

    """
    Copy the current board state this method is basically a helper method for HarderAi
    """

    def copy_board(self):
        copied_board = Board()
        copied_board.board = self.board[:]
        return copied_board

class InvalidChoiceError(Exception):

    """
    This class is just used to pass the invalid choice error and urge the player to valid choice
    """

    pass

class NotABoxNumberError(Exception):

    """
    Handle invalid box/board number exception
    """

    pass

def flip_icon(icon):

    """
    Flip coin method which will assign icon to the other player (computer or friend)
    """

    return ("X" if icon == "O" else "O")

def print_header():

    """
    Print game loading headers
    """

    print("""
     _____  _  ____     _____  ____  ____     _____  ____  _____
    /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    1 | 2 | 3
      / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      4 | 5 | 6
      | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     7 | 8 | 9
      \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____|

     To play Tic-Tac-Toe, you need to get three in a row...
     Your choices are defined, they must be from 1 to 9...
     """)

def get_score(result):

    """
    Show final result of the game
    """

    if result == "X":
        return "X won!"
    elif result == "O":
        return "O won"
    else:
        return "it's a draw"

def write_result_to_file(duration_string, statistic):

    """
    Write final detailed result of the game in file like how many times respective player win,
    what is the duration of game and current date etc.
    """

    with open("scores.txt", "a") as results_file:
        for player_name in statistic.keys():
            if player_name == 'draw':
                continue
            results_file.write("{} won {} number of times\n".format(player_name, statistic[player_name]))
        results_file.write("draws = {} times\n".format(statistic.get("draw", 0)))
        results_file.write("{}\n".format(duration_string))
        today = date.today()
        results_file.write(
            "This game was played on {}, {}, {}\n\n".format(today.day, calendar.month_name[today.month], today.year))

def get_duration_string(duration):

    """
    Calculate game duration in minutes and seconds
    """

    minutes = duration // 60
    seconds = duration % 60
    return "the game took {} minutes and {} seconds".format(minutes, seconds)

def main():

    """
    This main function is responsible for loading game, set player option, keep track of game etc.
    1st line of method is just to printing the game headers or welcome screen
    2nd line statistic object to keep track of each game states/result who win or draw etc.
    """

    print_header()
    statistic = {}


    while True:

        """
        System take input for opponent like friend or computer (computer is segregated into two types 'c1' (EasyAi) and 'c2' HarderAi)
        System also take input for player icon and provide only two options 'X' or 'O'
        """

        opponent = input(
            "Would you like to play against a friend or the computer? \n\t-friend (f)\n\t-computer level 1 (c1)\n\t-computer level 2 (c2)")
        icon_coice = input("Would you like to play as (X) or (O)? ").upper()
        players = [EasyAi(icon_coice), HarderAi(flip_icon(icon_coice))]
        if opponent.lower() == "f":
            players = [Human(icon_coice), Human(flip_icon(icon_coice))]
            # start a game with friend
        if opponent.lower() == "c1":
            players = [Human(icon_coice), EasyAi(flip_icon(icon_coice))]
            # start a game with computer
        if opponent.lower() == "c2":
            players = [Human(icon_coice), HarderAi(flip_icon(icon_coice))]

        start_time = time.time()

        """
        Load the Game by creating game class object and it takes the Players list
        call its play_game method to start game and return final results
        """

        game = Game(players=players)
        result = game.play_game()
        ending_time = time.time()

        statistic[result] = statistic.get(result, 0) + 1

        # calculate game duration
        duration = int(ending_time - start_time)
        duration_string = get_duration_string(duration)

        # pass the Game states and it duration to below method
        write_result_to_file(duration_string, statistic)

        user_choice = input("Would you like to play a game again? [y/n]")
        if user_choice.lower().startswith("n"):
            break


if __name__ == '__main__':
    sys.exit(main())

"""
Main function from where this code will start execute and call main function
"""