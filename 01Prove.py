'''
Solo Checkpoint 01
Author: Josh Dalton
'''

 
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
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    print("It's a draw!")
    return True

def game_won(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def take_turn(player, board):
    square = 0
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(player):
    if player != "x":
        return "x"

    else:
        return "o"

def main():
    play_again = "y"
    while play_again == "y":
        player = "x"
        board = new_board()
        while not (game_won(board) or cats_game(board)):
            display_board(board)
            take_turn(player, board)
            player = next_player(player)
        display_board(board)
        print("Good game. Thanks for playing!")
        play_again = input("Would you like to play again? (y/n): ").lower

    
if __name__ == "__main__":
    main()