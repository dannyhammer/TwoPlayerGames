##
# This class models a player for the Toothpick Takeaway game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Oct 7, 2020
##

class TakeawayPlayer:
    def __init__(self, player_name, strategy):
        """
        Instantiates a new TakeawayPlayer object.

        Parameters:
            player_name (string): Name of the player
            strategy (function): Function to determine what move to make

        Returns:
            A newly instatiated TakeawayPlayer
        """
        self.player_name = player_name
        self.strategy = strategy

    def move(self, board) -> int:
        """
        Makes a move based on the player's strategy.

        Parameters:
            board (TakeawayBoard): The board being played on

        Returns:
            A move based on the player's strategy
        """
        return self.strategy.move(board)
