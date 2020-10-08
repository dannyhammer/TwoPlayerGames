##
# This class models a Referee for the toothpick takeaway game.
#
# Authors: Daniel Hammer, Nihcolas O'Kelley, Andrew Shelton
#
# Date: Oct 7, 2020
##

import sys
sys.path.append("../generic_classes")
from referee import Referee

class TakeawayReferee(Referee):
    """The toothpick takeaway referee subclass."""

    def __init__(self, board):
        """ This class models a referee for a game.
        Args:
            none

        """
        Referee.__init__(self, board)

    def update_board(self, move, board) -> object:
        """ This method will handle updating the game board.

        Args:
            player : the current player making the move
            board : the game board
            move ; the move being made

        Return:
            The updated game board
        """

        board.state -= move
        return board


    def is_legal(self, board_state, move) -> bool:
        """ This function allows for the referee object to check if a move is
        valid.

        Args:
            board_state : the state of the board
            move  : the current move being made 

        Return:
            boolean : True or False depending on the move validity
        """
        is_within_range = move > 0 and move < 3
        is_not_too_many = board_state - move > -1
        return is_within_range and is_not_too_many

    def is_winning(self, board, move) -> bool:
        """A method to check if the current player is winning at a given 
        instance of the game.

        Args:
            board : the game board
            move : the current move

        Return:
            True or False based on the 'win condition'
        """

        # If the move depletes the number of toothpicks left to 0, it is winning
        return board.state - move == 0
