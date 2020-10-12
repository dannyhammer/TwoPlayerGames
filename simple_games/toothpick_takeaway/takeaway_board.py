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
        self.history = []

    def update(self, move):
        """ This function updates the board information once a player has 
        made a move.

        Args:
            none

        Return:
            none
        """
        self.history.append(move)

    def possible_moves(self):
        """ Returns a list of all possible moves given the current game state

        Args:
            none

        Returns:
            A list of all possible moves
        """

        available_moves = []
        if self.state == 0:
            available_moves.append(0)
        elif self.state == 1:
            available_moves.append(1)
        else:
            available_moves.extend([1, 2])

        return available_moves
