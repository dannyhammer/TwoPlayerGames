##
# This class models a game board for Toothpick Takeaway
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Oct 7, 2020
##
class TakeawayBoard:

    def __init__(self, num_toothpicks = 10):
        """ The board constructor initializes the current move set and game 
        state.

        Args:
            num_toothpicks : The number of toothpicks to start with
        Return:
            None
        """
        self.move_set = []
        self.state = num_toothpicks

    def update(self):
        """ This function updates the board information once a player has 
        made a move.

        Args:
            none

        Return:
            none
        """
        pass
