# Tic Tac Toe Game
# 1st Year CSE Project

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def show_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


def check_draw():
    return " " not in board


print("===== TIC TAC TOE =====")
print("Player 1 = X")
print("Player 2 = O")

current_player = "X"

while True:
    show_board()

    choice = input("Player " + current_player + ", choose a position (1-9): ")

    if not choice.isdigit():
        print("Please enter a number.")
        continue

    position = int(choice) - 1

    if position < 0 or position > 8:
        print("Choose a number between 1 and 9.")
        continue

    if board[position] != " ":
        print("That position is already taken.")
        continue

    board[position] = current_player

    if check_winner(current_player):
        show_board()
        print("Player " + current_player + " wins! 🎉")
        break

    if check_draw():
        show_board()
        print("It's a draw!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



