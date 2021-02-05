##
# This class models a Referee for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Referee:

    def __init__(self):
        """TODO: finished the referee constructor"""
        pass

    def is_legal(self, state, move):
        """ This function allows for the referee object to check if a move is
        valid.

        Args:
            state : the state of the board
            move  : the current move being made 

        Return:
            boolean : True or False depending on the move validity
        """
        pass

    def is_winning(self, state):
        """ This function determines the current player in the lead 

        Args:
            state : the state of the board

        Return:
            The player name of who is in the lead or wins the game 

        """
        pass
