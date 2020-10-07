##
# This class models a Referee for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Referee:

    def __init__(self):
        """ This class models a referee for a game.
        Args:
            none

        """
        self.is_game_over = False

    def update_board(self, board, player, other_player) -> object:
        """ This method will handle updating the game board.

        Args:
            board : the game board
            player : the current player making the move
            other_player : the player not making the move

        Return:
            The winning_player or None depending on the move update

        """
        pass

    def ask_for_move(self, board, player) -> str:
        """ This method takes in the board and current player and prompts for
        the next move.

        Then returns the move.

        Args:
            board : the game board
            player : player that is being prompted

        Return:
            The players move
        """
        pass

    def is_legal(self, board_state, move) -> bool:
        """ This function allows for the referee object to check if a move is
        valid.

        Args:
            board_state : the state of the board
            move  : the current move being made 

        Return:
            boolean : True or False depending on the move validity
        """
        pass

    def is_winning(self, board, move) -> bool:
        """A method to check if the current player is winning at a given 
        instance of the game.

        Args:
            board : the game board
            move : the current move

        Return:
            True or False based on the 'win condition'
        """
        pass
