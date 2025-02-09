# Function to create an empty 3x3 Tic-Tac-Toe board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        # Print the row elements separated by ' | '
        print(" | ".join(row))
        # Print a horizontal separator line after each row (except the first one)
        print("-" * 9)
