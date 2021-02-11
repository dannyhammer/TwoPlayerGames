import sys, os
sys.path.append(os.path.abspath("../classes/"))

from takeaway_board import TakeawayBoard
from takeaway_referee import TakeawayReferee
from takeaway_game import TakeawayGame
from takeaway_player import TakeawayPlayer
from takeaway_strategies import *

# Create a board of 10 toothpicks
my_board = TakeawayBoard(10)
# Create a referee to govern the board
my_referee = TakeawayReferee(my_board)

# Create two random move players
random_player_1 = TakeawayPlayer(player_name = "player_1", strategy = random_move)
random_player_2 = TakeawayPlayer(player_name = "player_2", strategy = random_move)

# Create the game
my_game = TakeawayGame(board = my_board,
                       referee = my_referee,
                       players = [random_player_1, random_player_2])

# Play the game
winner, history = my_game.play(narrated = False)

# Display data
print("\nWinning player is:", winner.player_name)
for toothpicks, data in history.items():
    print("Toothpicks left:", toothpicks, " | Data:", data)
