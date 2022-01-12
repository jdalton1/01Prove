'''
Solo Checkpoint 01
Author: Josh Dalton
'''

def main():
    player = next_player("")
    board = new_board()
    while not (game_won(board) or cats_game(board)):
        take_turn(player, board)
        display_board(board)

def new_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def cats_game(board):
    return


def game_won(board):
    return

def take_turn(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(player):
    if player == "" or player == "x":
        return "o"
    elif player == "o":
        return "x"

main()