This is a simple Tic-Tac-Toe game implemented in Python. It supports two players playing on the same device, randomly selecting the first player and allowing each player to choose their symbol (either 'X' or 'O'). The game ends when one player wins or if the board is full (a draw).

Features

2-player gameplay: Play with a friend on the same computer.
Randomly selected first player: The first player is chosen randomly.
Symbol selection: Players can choose either 'X' or 'O'.
Game over conditions: The game checks for a winner or draw after every move.
Board display: The current state of the board is shown after every move.

Game Flow

The game will randomly choose which player goes first.
The first player will select either 'X' or 'O', and the second player will automatically get the opposite symbol.
Players will take turns to enter the row and column (from 0 to 2) to place their symbol on the board.
After each move, the board is displayed, and the game checks if there's a winner or if the game ends in a draw.
The game ends when a player wins or when there are no more valid moves left (draw).

How to Play

After running the game, the first player is randomly selected.
Players will then be asked to choose their symbol ('X' or 'O'). The second player gets the opposite symbol automatically.
Players will take turns entering the row and column where they want to place their symbol.
The board will be displayed after every move.
The game will announce the winner or a draw when the game ends.

File Structure

main.py: The main file where the game logic is executed.
board_system.py: Contains functions to manage the board (create and display the board).
win_conditions.py: Contains functions to check if a player has won or if the game is a draw.
players_system.py: Contains functions for choosing the first player and selecting symbols.
