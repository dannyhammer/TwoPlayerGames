##
# This class models a player for the Toothpick Takeaway game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Oct 7, 2020
##

import random

class TakeawayPlayer:

    def __init__(self, strategy = None, player_name):
        """ The player constructor

        Args:
            player_num : The player number in the game
            is_human : Whether or not the player is human-controlled

        Return:
            None 
        """
        self.player_name = player_name
        self.strategy = strategy

    def move(self, board):
        """ This function takes in a board and then allows the player to make
        a choice on the next move.

        Args:
            board : the board with the tooth picks

        Return:
            string : the move made (take 1 or 2 toothpicks)
        """

        move = strategy(board)

        return move
