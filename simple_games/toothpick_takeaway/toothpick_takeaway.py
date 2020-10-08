##
# This file runs a simulation of many Toothpick Takeaway games
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Oct 7, 2020
##

# Necessary imports
from takeaway_player import TakeawayPlayer
from takeaway_referee import TakeawayReferee
from takeaway_board import TakeawayBoard
from takeaway_game import TakeawayGame

# Get the number of games to run
# This may need to have the human component removed
games_to_run = int(input("Enter the number of games to run > "))

# Create a human player
player1 = TakeawayPlayer(player_num = 1, is_human = False, strategy = None)

# Create a computer player
player2 = TakeawayPlayer(player_num = 2, is_human = False, strategy = None)

# Assemble player list
player_set = [player1, player2]

# Construct a board
toothpicks = TakeawayBoard(num_toothpicks = 10)

# Obtain a referee
pickmaster = TakeawayReferee(toothpicks)

# Create a game
game = TakeawayGame(board = toothpicks, referee = pickmaster, players = player_set)

# Obtain the winner data from 1,000 games
winner_data =  [game.play().player_num for x in range(games_to_run)]

print("Winner Data:", winner_data)
