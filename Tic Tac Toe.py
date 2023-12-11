# This function is dispalying the tic tac toe board
def display_board(board):
    print("+" + "-" * 13 + "+")  # to display the top border
    for i, row in enumerate(board):
        print("|", end=" ")
        for j, cell in enumerate(row):
            print(cell, end=" | ")
        print("\n" + "+---+---+---+")  # right border
    print()


# To get player's row and column choices

def get_player_choice():
    try:  # to handle potential errors in user input
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        return row, col
    except ValueError:  # if a user entered non-numeric value
        print("Invalid input. Please enter a number.")
        return get_player_choice()


# A function to place/represent a player's mark on the board
def place_mark(board, player, position):
    row, col = position
    if board[row][col] == " ":  # check if chosen place is empty
        board[row][col] = player
        return True
    else:
        print("Invalid move. Try again.")
        return False


# A Function to check player's win or not
def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Main game loop
def tic_tac_toe():
    # Initialize the game board and current player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        # Display the current state of the board
        display_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's row and column choice
        position = get_player_choice()
        if place_mark(board, current_player, position):
            # Display the updated board and the move
            display_board(board)
            print(f"Player {current_player} marked {current_player} at ({position[0]}, {position[1]})\n")

            # Check for a winner or a tie
            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print("It's a tie!")
                break

            # Switch to the other player for the next turn
            current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    # Start the Tic Tac Toe game
    tic_tac_toe()
