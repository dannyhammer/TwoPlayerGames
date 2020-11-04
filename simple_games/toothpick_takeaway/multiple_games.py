from takeaway_board import TakeawayBoard
from takeaway_referee import TakeawayReferee
from takeaway_game import TakeawayGame
from takeaway_player import TakeawayPlayer
from takeaway_strategies import *

# We're going to collect a lot of data
game_data = []
# Run ten games on each board
num_games = 10
board_sizes = range(1, 100)

# Run a set number of games for each board
for board in board_sizes:
    # Create a board of  toothpicks
    my_board = TakeawayBoard(board)
    # Create a referee to govern the board
    my_referee = TakeawayReferee(my_board)

    # Create two players; one always takes 1, the other moves randomly
    random_player_1 = TakeawayPlayer(player_name = "player_1", strategy = always_take_one)
    random_player_2 = TakeawayPlayer(player_name = "player_2", strategy = random_move)

    for game in range(num_games):
        # Create the game
        my_game = TakeawayGame(board = my_board,
                               referee = my_referee,
                               players = [random_player_1, random_player_2])

        # Play the game
        winner, history = my_game.play(narrated = False)
        game_data.append((winner.player_name, history))

import pandas as pd
games_df = pd.DataFrame(game_data,columns=['Winner', 'player_state_i'])
games_df.to_csv("test.csv", index = False)

# Display data
#for game in game_data:
    #winner, history = game
    #print("\nWinning player is:", winner.player_name)
    #for toothpicks, data in history.items():
    #    print("Toothpicks left:", toothpicks, " | Data:", data)
