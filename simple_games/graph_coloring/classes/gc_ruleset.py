##
# Two players attempt to color a graph with `n` available colors.
# Player 1's goal is to fully color the graph.
# Player 2's goal is to stop Player 1 from fully coloring the graph.
# A node can be colored a given color if and only if none of its neighbors
# are already that color.
# Players alternate coloring nodes until the end of the game is reached.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-27
##

import sys
sys.path.append("../..")
from generic_classes.ruleset_interface import RulesetInterface

class GCRuleset(RulesetInterface):

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
        A move is legal if and only if none of the neighboring vertices are
        already colored with the attempted coloring.
        For example, if vtx #1 has a neighbor that is green, vtx #1 cannot be green.

        Args:
            board : The board being played on
            proposed_move : The move being proposed

        Return:
            True if the move was legal, else False.
        """
        if not proposed_move:
            return False

        # If the vertex was not uncolored, the move is invalid
        if board.state[proposed_move["vertex"]]["color"] != 0:
            return False

        # Otherwise, iterate over the neighbors of the vertex
        for neighbor in board.state[proposed_move["vertex"]]["adj"]:
            # If any of the neighbors are colored with the same color,
            # the move is invalid
            if board.state[neighbor]["color"] == proposed_move["color"]:
                return False

        return True

    def is_game_over(self, board):
        """
        Determines if the game is over.
        The game is over when either the graph is fully colored,
        or there exist a node that cannot be colored.

        Args:
            board : The board being played on

        Return:
            True if the state of the board is an end-game state, else False.
        """
        # Case 1: The graph is entirely colored; Player 1 wins
        vertex_colors = [board.state[vtx]["color"] for vtx in range(len(board.state))]
        if 0 not in vertex_colors:
            return True

        # Case 2: The graph is in a state in which it is impossible to color any more vertices; Player 2 wins
        game_colors = range(1, board.bounds + 1)
        for vtx in range(len(board.state)):

            # If there exists an uncolored vertex
            if board.state[vtx]["color"] == 0:

                # Get the colors of all the neighbors
                neighbor_colors = [board.state[neighbor]["color"] for neighbor in board.state[vtx]["adj"]]
                # Get the valid colors for the current vertex
                valid_colors = list(set(game_colors) - set(neighbor_colors))
                # If there are no valid colors, the game is over
                if len(valid_colors) == 0:
                    return True

        return False

    def update_board(self, board, player, move):
        """
        Update the board based on the player's given move.
        Also updates the board's `data` field to log move history.

        Args:
            board : The board being played on
            player : The player who made the move
            move : The move being made
        """
        board.data[str(board.state)] = (player.name, move)

        board.state[move["vertex"]]["color"] = move["color"]

    def declare_winner(self, board, players):
        """
        Declare a winner based on the board's current state.
        If there are no more uncolored vertices, Player 1 wins.
        Otherwise, Player 2 wins.

        Args:
            board : The board being played on
            players : List of players in the game

        Return:
            The winning player of the game
        """
        if 0 not in [board.state[vtx]["color"] for vtx in range(len(board.state))]:
            winner = players[0]
        else:
            winner = players[1]

        return winner
