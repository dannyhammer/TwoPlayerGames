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

    def __str__(self):
        """
        Overrides the default implementation of `str()`.
        Provides a more readable way of printing players.

        Return:
            A formatted string containing the player's name and strategy's info
        """
        string = "{}: {}".format(self.name, self.strategy.name)

        # If strategy data is available, display it
        if self.strategy.data:
            string = "{}: {}".format(string, self.strategy.data)

        return string
