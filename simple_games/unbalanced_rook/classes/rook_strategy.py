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
sys.path.append("../..")
from src.strategy_interface import StrategyInterface

class RookStrategy(StrategyInterface):

    def move(self, board):
        """
        Make a move based on the strategy.

        Args:
            board : The board being played on

        Return:
            A proposed move.
        """
        direction = random.choice(["D", "R"])

        # Gets the max number of tiles possible to move
        max_tiles = board.bounds[direction] - board.state[direction]
        if max_tiles < 1:
            return None
        move = random.randrange(1, max_tiles + 1)

        return {"direction": direction, "tiles": move}
