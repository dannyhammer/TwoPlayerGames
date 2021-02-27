##
# Simple Smart Strategy
# Searches uncolored vertices and attempts to color with the remaining legal colors.
# This strategy is pseudo-smart as it will never attempt an illegal coloring,
# However, it cannot always guarantee a move. 
# If no legal coloring is available, it will simply return None.
# It is also somewhat random, as it randomly chooses a legal color.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-27
##

from random import choice

import sys
sys.path.append("../..")
from generic_classes.strategy_interface import StrategyInterface

class GCSimpleSmartStrategy(StrategyInterface):

    def __init__(self, name, data = None):
        """
        Strategy constructor.

        Args:
            name : The name of the strategy
            data : (Optional) Data to read from to influence moves.
        """
        self.name = name
        self.data = data

    def move(self, board):
        """
        Make a move based on colors available.
        This is psuedo-smart in the sense that it attempts to choose the lowest-index
        vertex and colors it with the lowest-value available color in the list.

        Args:
            board : The board being played on

        Return:
            A proposed move.
        """
        game_colors = range(1, board.bounds + 1)
        for vtx in range(len(board.state)):
            if board.state[vtx]["color"] == 0:
                # Get the colors of all the neighbors
                neighbor_colors = [board.state[neighbor]["color"] for neighbor in board.state[vtx]["adj"]]
                # Get the valid colors for the current vertex
                valid_colors = list(set(game_colors) - set(neighbor_colors))

                # Choose a color from the remaining available (currently random)
                try:
                    color = choice(valid_colors)

                    return {"vertex": vtx, "color": color}
                except:
                    # If there are no valid colors, check the next vertex
                    continue

        return None
