from board_system import display_board, create_board
from win_conditions import check_winner, check_draw, is_game_over
from players_system import choose_player, choose_symbol

players = ["Player_1", "Player_2"]
# Dictionary to store assigned symbols (X or O)
player_options = {}

# Initialize the game board as a 3x3 grid with empty spaces
board = create_board()

# Randomly selecting which player goes first
current_player = choose_player(players)

# Changing the players lif if Player 2 was chosen to go first
if current_player == players[1]:
    # Swaps the order if Player 2 was chosen first
    players.reverse()

# Allow the first player to choose their symbol, assigning the opposite to the second player
player_options = choose_symbol(players, player_options)


# Function to get a valid move from the player
def get_empty_cell():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2):"))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            print("Invalid or occupied cell, try again.")
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")


while not is_game_over(board):
    display_board(board)
    print(f"It's {current_player}'s turn!")
    option = player_options[current_player]
    row, col = get_empty_cell()
    board[row][col] = option

    if check_winner(board):
        display_board(board)
        print(f"{current_player} wins!")
        break
    elif check_draw(board):
        display_board(board)
        print("It's a draw!")
        break
    current_player = players[1] if current_player == players[0] else players[0]

display_board(board)
