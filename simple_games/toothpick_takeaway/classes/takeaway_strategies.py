##
# This represents a strategy that can be used in determining moves.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Nov 30, 2020
##

from random import choice

class TakeawayStrategy:
    def __init__(self, name = "random", data = None, bias = None):
        """
        Instantiates a new TakeawayStrategy object.

        Parameters:
            name (string): The name of the strategy to use
            data (DataFrame): Move data
            bias (int): What move the strategy defaults to, if any

        Returns:
            A newly instatiated TakeawayStrategy
        """
        self.name = name
        self.data = data
        self.bias = bias
        self.strategies = {"random": self.random_move,
                           "take_one": self.always_take_one,
                           "take_two": self.always_take_two,
                           "smart": self.smart_move,
                           "human": self.human
                          }

    def move(self, board) -> int:
        """
        Makes a move based on the current strategy.

        Parameters:
            board (TakeawayBoard): The board being played on

        Returns:
            A move to try
        """
        deciding = True
        possible_moves = board.possible_moves()
        moves_tried = []
        attempts = 1
        move_to_try = 0
        while deciding:
            # Get a move
            move_to_try = self.strategies[self.name](board, possible_moves)

            # If the move is invalid, note it and re-loop
            # Otherwise, end the loop
            if (board.state - move_to_try) < 0:
                moves_tried.append(move_to_try)
                attempts += 1
            else:
                deciding = False

            # If all possible moves have been tried or 3 attempts have been made
            if set(moves_tried) == set(possible_moves) or attempts == 3:
                deciding = False
                move_to_try = 0

        return move_to_try

    def smart_move(self, board, possible_moves) -> int:
        """
        Moves intelligently based on previous game data.

        Parameters:
            board (TakeawayBoard): The board being played on
            possible_moves (list): All possible moves on the current state of the board

        Returns:
            A move to try
        """
        # Get the otpimal move
        move_to_try = 1 if self.data["Take 1"][board.state] > self.data["Take 2"][board.state] else 2

        # If both chances are equal, choose randomly or according to a bias, if supplied
        if self.data["Take 1"][board.state] == self.data["Take 2"][board.state]:
            move_to_try = choice(possible_moves) if self.bias is None else self.bias

        # If the move is not legal, mark it as tried and pick the only other option
        if (board.state - move_to_try) < 0:
            possible_moves.remove(move_to_try)
            move_to_try = possible_moves[0]

        # If the only other move available is invalid, return None
        if (board.state - move_to_try) < 0:
            return 0

        return move_to_try

    def random_move(self, board, possible_moves) -> int:
        """
        Moves randomly based on available moves.

        Parameters:
            board (TakeawayBoard): The board being played on
            possible_moves (list): All possible moves on the current state of the board

        Returns:
            A move to try
        """
        return choice(possible_moves)

    def always_take_one(self, board, possible_moves) -> int:
        """
        Always takes 1 toothpick.

        Parameters:
            board (TakeawayBoard): The board being played on
            possible_moves (list): All possible moves on the current state of the board

        Returns:
            1, to take 1 toothpick
        """
        return 1

    def always_take_two(self, board, possible_moves) -> int:
        """
        Always takes 2 toothpicks.

        Parameters:
            board (TakeawayBoard): The board being played on
            possible_moves (list): All possible moves on the current state of the board

        Returns:
            2, to take 2 toothpicks
        """
        return 2

    def human(self, board, possible_moves) -> int:
        """
        Requests human input to decide a move.

        Parameters:
            board (TakeawayBoard): The board being played on
            possible_moves (list): All possible moves on the current state of the board

        Returns:
            A move to try
        """
        return int(input("Please make your move > "))
