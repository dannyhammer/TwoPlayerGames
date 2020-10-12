##
# This class models a player for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Player:

    def __init__(self, strategy = lambda x: pass, player_name):
        """ The player constructor

        Args:
            player_num : the player number in the game

        Return:
            None 
        """
        self.player_name = player_name
        self.strategy = strategy

    def move(self, board):
        """ This function takes in a board and then allows the player to make
        a choice on the next move.

        Args:
            board : the board object for the current game

        Return:
            The move made.
        """
        pass
