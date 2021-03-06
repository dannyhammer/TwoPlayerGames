##
# Randomly Initialized Strategy
# Generates random vertex and color orderings on initialization
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-27
##

from random import sample

import sys
sys.path.append("../..")
from classes.strategy_interface import StrategyInterface

class GCRandomInitStrategy(StrategyInterface):

    def __init__(self, name, data = None):
        """
        Strategy constructor.

        Args:
            name : The name of the strategy
            data : (Optional) Data to read from to influence moves.
        """

        # Shuffle the orderings in the data
        new_data = {}
        for key in list(data.keys()):
            new_data[key] = sample(data[key], len(data[key]))

        self.name = name
        self.data = new_data

    def move(self, board):
        """
        Attempts to make a move by following the vertex coloring provided by
        the `data` field.

        Args:
            board : The board being played on

        Return:
            A proposed move.
        """
        # Iterate over the vertex ordering
        for vtx in self.data["vertices"]:
            # If the vertex is uncolored
            if board.state[vtx]["color"] == 0:
                # Get the vertex's neighbors' colors
                adj_colors = [board.state[adj]["color"] for adj in board.state[vtx]["adj"]]

                # Iterate over the color ordering
                for color in self.data["colors"]:

                    # If the color is available, use it
                    if color not in adj_colors:
                        return {"vertex": vtx, "color": color}

        return None
