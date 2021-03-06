##
# This interface lists the required functions to define a strategy for a game.
# More helper functions can be made, depending on the game's complexity.
# The constructor takes in a `data` parameter, which should be a dictionary
# to pull move data from. If the player wants to be smart with this strategy,
# the board data and strategy data will need to be analyzed in the `move()`
# method to determine an optimal move.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##

class StrategyInterface:

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
        Make a move based on the strategy.

        Args:
            board : The board being played on

        Return:
            A proposed move.
        """
        pass

    def set_name(self, name):
        """
        Update the strategy's name.

        Args:
            name : New name of the strategy
        """
        self.name = name

    def set_data(self, data):
        """
        Update the strategy's data.

        Args:
            data : The new data to apply to the strategy
        """
        self.data = data

    def __str__(self):
        """
        Overrides the default implementation of `str()`.
        Provides a more readable way of printing strategies.

        Return:
            A formatted string containing the strategy's name and info
        """
        string = self.name

        # If strategy data is available, display it
        if self.data:
            string = "{}: {}".format(string, self.data)

        return string

    def __eq__(self, other):
        """
        Overrides the default implementation of `==`.
        Provides a way of comparing strategies.

        Args:
            other : The strategy being compared with

        Return:
            True if the strategies contain the same data, else False
        """
        if isinstance(other, StrategyInterface) and self.data and other.data:
            return self.data == other.data

        return False

    def __ne__(self, other):
        """
        Overrides the default implementation of `!=`.
        Provides a way of comparing strategies.

        Args:
            other : The strategy being compared with

        Return:
            True if the strategies contain the same data, else False
        """
        if isinstance(other, StrategyInterface) and self.data and other.data:
            return self.data != other.data

        return False

