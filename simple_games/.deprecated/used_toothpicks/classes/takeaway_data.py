##
# This encapsulates Toothpick Takeaway game data.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Nov 30, 2020
##

class TakeawayData:
    def __init__(self):
        """
        Instantiates a new TakeawayData object.

        Returns:
            A newly instantiated TakeawayData
        """
        self.history = {}
        self.winner = None

    def record_move(self, toothpicks_left, player, move):
        """
        Inserts a given move into the game data.

        Parameters:
            toothpicks_left (int): Number of toothpicks left on the table
            player (TakeawayPlayer): The player making the move
            move (int): The move being made
        """
        self.history[toothpicks_left] = {"name": player.player_name, "move": move}

    def reset(self):
        """
        Resets the game data.
        """
        self.history = {}
        self.winner = None
