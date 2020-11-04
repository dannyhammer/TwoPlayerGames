##
# Master Script
# 
# Just call `run_game` with the appropriate parameters
# Comment/uncomment calls as needed
##
from base_script import run_game

"""
run_game(num_games: int
          board_sizes: list
          p1_strategy: string
          p2_strategy: string)
"""

run_game(100, range(100), "random", "random")

run_game(100, range(100), "take_one", "random")
run_game(100, range(100), "random", "take_one")

run_game(100, range(100), "take_two", "random")
run_game(100, range(100), "random", "take_two")

run_game(1, range(100), "take_one", "take_two")
run_game(1, range(100), "take_two", "take_one")
