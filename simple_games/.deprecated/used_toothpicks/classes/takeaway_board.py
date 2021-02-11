##
# This class models a game board for Toothpick Takeaway
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Oct 7, 2020
##

from takeaway_data import TakeawayData

class TakeawayBoard:
    def __init__(self, num_toothpicks = 10):
        """
        Instantiates a new TakeawayBoard object.

        Parameters:
            num_toothpicks (int): The number of toothpicks on the board

        Returns:
            A newly instatiated TakeawayBoard
        """
        self.state = num_toothpicks
        self.initial_size = num_toothpicks
        self.summary = TakeawayData()

    def possible_moves(self) -> list:
        """
        Returns a list of all possible moves.

        Returns:
            A list representing all possible moves at the current state of the board
        """
        return [1, 2] if self.state > 1 else [1]

    def reset(self):
        """
        Resets the game board.
        """
        self.state = self.initial_size
        self.summary = TakeawayData()
