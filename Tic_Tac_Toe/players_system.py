# Function to randomly choose which player goes first
def choose_player(players):
    import random
    # Select a random player from the list
    first = random.choice(players)
    print(f"Your turn {first}.")
    # Return the selected player
    return first


# Function to let the first player choose their symbol (X or O)
def choose_symbol(players_list, player_options):
    while True:
        # Prompt the first player to choose a symbol
        option = input(f"{players_list[0]}, choose your symbol (X or O): ").strip().upper()
        # Checking if the input is valid
        if option in ["X", "O"]:
            # Assign the chosen symbol to the first player
            player_options[players_list[0]] = option
            # Assign the opposite symbol to the second player
            player_options[players_list[1]] = "O" if option == "X" else "X"
            # Printing confirmation message
            print(f"{players_list[0]} has chosen {option}."
                  f" {players_list[1]} is automatically assigned {player_options[players_list[1]]}.")
            # Exiting the loop once a valid choice is made
            break
        else:
            print("Invalid choice. Please choose X or O.")
    # Returning the updated player symbols dictionary
    return player_options
