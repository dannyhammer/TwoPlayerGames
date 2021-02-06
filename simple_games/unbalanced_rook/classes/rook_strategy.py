##
# Defines the strategy used by a player to make a move for Unbalanced Rook.
# More helper functions can be made, depending on the strategy's complexity.
# The constructor takes in a `data` parameter, which should be a dictionary
# to pull move data from. If the player wants to be smart with this strategy,
# the board data and strategy data will need to be analyzed in the `move()`
# method to determine an optimal move.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##

import random
import sys
sys.path.append("..")
from generic_classes.strategy_interface import StrategyInterface

class RookStrategy(StrategyInterface):

    def __init__(self, name, data = None):
        """
        Strategy constructor.

        Args:
            name : The name of the strategy
            data : Data to read from, if applicable
        """
        self.name = name
        self.data = data

    def move(self, board):
        """
        Make a move based on the strategy.

        Args:
            board : The board being played on

        Return:
            A proposed move.
        """
        direction = random.choice(["D", "R"])

        # Smart-ish Move. Counts the `n` remaining spaces in a direction and
        # moves within a range of 0-n+1. Can cause rook to move too far
        max_tiles = board.bounds[direction] - board.state[direction] + 1
        move = random.randrange(0, max_tiles + 1)

        return {"direction": direction, "tiles": move}
