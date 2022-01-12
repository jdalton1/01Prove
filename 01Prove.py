'''
Solo Checkpoint 01
Author: Josh Dalton
'''

def main():
    player = next_player("")
    board = new_board()

    return 

def new_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("--+--+--")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("--+--+--")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def cats_game():
    return


def game_won():
    return

def take_turn():
    return

def next_player():
    return

