##
# This class models a game board for most two player games.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##
class Board:

    def __init__(self, initial_state = None, bounds = None):
        """
        The board constructor initializes the game state and sets game bounds.

        Args:
            initial_state : The initial game state
            bounds : The bounds of the board, if applicable (size, minimum, etc.)
        """
        self.initial_state = initial_state
        self.state = initial_state
        self.bounds = bounds
        self.data = {}

    def reset(self):
        """
        Resets the board to its original state.
        """
        self.state = self.initial_state
        self.data = {}
