##
# This interface lists the required functions to define a ruleset for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##
class RulesetInterface:

    def __init__(self, name, initial_state, bounds = None):
        """
        Rulset constructor.

        Args:
            name : The name of the ruleset
            initial_state : The initial state of the board
            bounds : (Optional) The bounds of the board
        """
        self.name = name
        self.initial_state = initial_state
        self.bounds = bounds

    def is_legal(self, board, proposed_move):
        """
        Determines if the move proposed is legal.

        Args:
            board : The board being played on
            proposed_move : The move being proposed

        Return:
            True if the move was legal, else False.
        """
        pass

    def is_game_over(self, board):
        """
        Determines if the game is over.

        Args:
            board : The board being played on

        Return:
            True if the state of the board is an end-game state, else False.
        """
        pass

    def update_board(self, board, player, move):
        """
        Update the board based on the player's given move.
        Also updates the board's `data` field to log move history.

        Args:
            board : The board being played on
            player : The player who made the move
            move : The move being made
        """
        pass

    def declare_winner(self, board, players):
        """
        Declare a winner based on the board's current state.
        In many cases, the winner will simply be whoever made the most recent move.
        However, for more complex games, the board's state will need to be considered

        Args:
            board : The board being played on
            players : List of players in the game

        Return:
            The winning player of the game
        """
        pass
