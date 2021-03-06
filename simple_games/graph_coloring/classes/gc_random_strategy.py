##
# Random Strategy
# Randomly chooses a vertex and color.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-27
##

from random import randrange

import sys
sys.path.append("../..")
from src.strategy_interface import StrategyInterface

class GCRandomStrategy(StrategyInterface):

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
        Randomly pick a vertex and color

        Args:
            board : The board being played on

        Return:
            A proposed move.
        """
        vtx = randrange(0, len(board.state))
        color = randrange(1, board.bounds + 1)
        return {"vertex": vtx, "color": color}
