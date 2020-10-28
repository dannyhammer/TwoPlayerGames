##
# This class models a game board for most two player games.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Board:

    def __init__(self, initial_state = None):
        """ The board constructor initializes the current move set and game 
        state.

        Args:
            initial_state : The initial game state
        Return:
            A new and initialized Board instance
        """
        self.initial_state = initial_state
        self.state = initial_state
