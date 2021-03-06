##
# A number of toothpicks is placed on a board.
# Players alternate picking up one or two toothpicks each turn.
# The player who removes the last toothpick is the winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-10
##

import sys
sys.path.append("../..")
from src.ruleset_interface import RulesetInterface

class ToothpickRuleset(RulesetInterface):

    def __init__(self, name, initial_state = 10, bounds = 2):
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
        if proposed_move is None:
            return False

        return proposed_move > 0 and proposed_move <= min(board.bounds, board.state)

    def is_game_over(self, board):
        """
        Determines if the game is over.

        Args:
            board : The board being played on

        Return:
            True if the state of the board is an end-game state, else False.
        """
        return board.state == 0

    def update_board(self, board, player, move):
        """
        Update the board based on the player's given move.
        Also updates the board's `data` field to log move history.

        Args:
            board : The board being played on
            player : The player who made the move
            move : The move being made
        """
        board.data[board.state] = (player.name, move)
        board.state -= move

    def declare_winner(self, board, players):
        """
        Declare a winner based on the board's current state.
        The last entry is the last player who made a legal move,
        and is therefore the winner of the game

        Args:
            board : The board being played on
            players : List of players in the game

        Return:
            The winning player of the game
        """
        last_entry = list(board.data.values())[-1][0]

        return players[0] if players[0].name is last_entry else players[1]

