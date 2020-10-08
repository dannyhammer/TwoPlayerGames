##
# This class models a player for the Toothpick Takeaway game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Oct 7, 2020
##

import random

class TakeawayPlayer:

    def __init__(self, player_num = 1, is_human = False, strategy = None):
        """ The player constructor

        Args:
            player_num : The player number in the game
            is_human : Whether or not the player is human-controlled

        Return:
            None 
        """
        self.player_num = player_num
        self.is_human = is_human
        self.strategy = strategy

    def move(self, board):
        """ This function takes in a board and then allows the player to make
        a choice on the next move.

        Args:
            board : the board with the tooth picks

        Return:
            string : the move made (take 1 or 2 toothpicks)
        """

        move = None

        if self.is_human:
            # Human-in-the-loop
            move = int(input("Enter your move > ").strip())

        else:
            # Automatic moves, randomly determined
            if self.strategy == None:
                move = random.randint(1, 2)

        return move
