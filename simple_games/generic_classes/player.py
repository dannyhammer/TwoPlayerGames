##
# This class models a player for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##
class Player:

    def __init__(self, name, strategy):
        """
        The player constructor.

        Args:
            name: The player's label
            strategy: A strategy function used by the player
        """
        self.name = name
        self.strategy = strategy

    def move(self, board):
        """
        This function takes in a board and then allows the player to make a
        choice on the next move.

        Args:
            board : The board object for the current game

        Return:
            The move made.
        """
        return self.strategy.move(board)
