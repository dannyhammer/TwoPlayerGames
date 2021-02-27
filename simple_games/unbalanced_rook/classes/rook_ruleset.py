##
# Defines the rules for the game of Unbalanced Rook.
# The game starts with a tileboard of size `n` x `n` with a Rook at position 0,0
# Players alternate moving the right any number of spaces either RIGHT or DOWN.
# Players cannot move two directions in the same turn and cannot move beyond the
# bounds of the board. The game ends when either a player submits an invalid
# move or the player moves the Rook to position `n`,`n`.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##

import sys
sys.path.append("..")
from generic_classes.ruleset_interface import RulesetInterface

class RookRuleset(RulesetInterface):

    def __init__(self, name, initial_state = {"D": 0, "R": 0}, bounds = {"D": 10, "R": 10}):
        """
        Ruleset constructor.

        Args:
            name : The name of the ruleset
            initial_state : The initial state of the board
            bounds : The bounds of the board
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
            True if the move's direction is Down or Right AND it is within
            bounds of the board
        """
        legal = False

        # Check if the move supplied exists and is above 0
        if (not proposed_move or not proposed_move["tiles"] or
                not proposed_move["direction"] or proposed_move["tiles"] < 1):
            return legal

        if proposed_move["direction"] == "D":
            legal = board.state["D"] + proposed_move["tiles"] <= board.bounds["D"]
        elif proposed_move["direction"] == "R":
            legal = board.state["R"] + proposed_move["tiles"] <= board.bounds["R"]

        return legal

    def is_game_over(self, board):
        """
        Determines if the game is over.

        Args:
            board : The board being played on

        Return:
            True if the current board state is its bounds (rook is at the end of
            the board).
        """
        return board.state == board.bounds

    def update_board(self, board, player, move):
        """
        Updates the rook's position on the board by applying the move's
        direction and number of tiles.
        Also updates the board's history, using the game state as an index.

        Args:
            board : The board being played on
            player : The player who made the move
            move : The move being made
        """
        state = "{},{}".format(board.state["D"], board.state["R"])
        board.data[state] = (player.name, move)

        board.state[move["direction"]] += move["tiles"]

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
