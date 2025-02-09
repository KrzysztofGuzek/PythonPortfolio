# Function to check if there is a winner on the board
def check_winner(board):
    # Checking each row for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            # Returning the winner (X or O) if all cells in the row match
            return board[i][0]
    # Checking the diagonal from top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        # Returning the winner if diagonal matches
        return board[0][0]
    # Checking the diagonal from top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    # If no winner is found, returns None
    return None


# Function to check if the game is a draw (no empty spaces left on the board)
def check_draw(board):
    for row in board:
        # If there's any empty space, return False (game isn't over)
        if " " in row:
            return False
    # If no empty spaces are found, return True (draw)
    return True


# Function to check if the game is over (either a win or a draw)
def is_game_over(board):
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
        return True
    if check_draw(board):
        print("It's a draw!")
        return True
    # If neither condition is met, return False (game continues)
    return False
