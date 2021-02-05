##
# This class models a game board for most two player games.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Board:

    def __init__(self, size):
        """ The board constructor initializes the current move set and game 
        state.

        Args:
            None
        Return:
            None
        """

        self.board = [[False for i in range(size)] for j in range(size)]
        self.size = size

    def update(self):
        """ This function updates the board information once a player has 
        made a move.

        Args:
            none

        Return:
            none
        """
        pass
