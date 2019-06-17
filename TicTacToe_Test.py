from TicTacToe import *

if __name__ == '__main__':
    board = Board()
    print(board.get_open_spaces())
    assert board.get_open_spaces() == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board.player_move(0, 'X')
    assert board.get_open_spaces() == [1, 2, 3, 4, 5, 6, 7, 8]
    print(board.__str__())
    assert board.__str__() == "\n X |   |   \n   |   |   \n   |   |   \n"
    board = Board()
    board.board = board.board = ['X',' ',' ',' ','X',' ',' ',' ','X']
    assert board.is_victory("X")
    assert not board.is_victory("O")
    board.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
    assert board.is_victory("X")
    assert not board.is_victory("O")