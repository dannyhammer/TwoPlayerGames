##
# This class models a Referee for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Sep 22, 2020
##

from takeaway_player import TakeawayPlayer

class TakeawayReferee:
    def __init__(self, board):
        """
        Instantiates a new TakeawayReferee object.

        Parameters:
            board (TakeawayBoard): The board being played on

        Returns:
            A newly instatiated TakeawayReferee
        """
        self.is_game_over = False
        self.board = board

    def update(self, player) -> int:
        """
        Executes a 'turn' of the game by asking for a move, applying that move, and updating the game history.

        Parameters:
            player (TakeawayPlayer): The player making the current move

        Returns:
            The move made at the current turn
        """
        # Get current (legal) move
        current_move = self.ask_for_move(player)

        # Record the move history
        self.board.summary.record_move(self.board.state, player, current_move)

        # Update game board
        self.board.state -= current_move

        return current_move

    def ask_for_move(self, player) -> int:
        """
        Requests a move from the current player.

        Parameters:
            player (TakeawayPlayer): The player making the current move

        Returns:
            The proposed move to make
        """
        # To check for repeats
        deciding = True

        while deciding:
            # See what move the player would want to make.
            proposed_move = player.move(self.board)

            # Check to see if player has given up
            if proposed_move == 0 or proposed_move is None:
                deciding = False
                proposed_move = 0

            # If the move was legal, exit the loop
            elif self.is_legal(proposed_move):
                deciding = False

        return proposed_move

    def is_legal(self, move) -> bool:
        """
        Determines if a move is legal to make.

        Parameters:
            move (int): The proposed move to check the legality of

        Returns:
            True if the move is legal, else false
        """
        return ((move > 0) and (move < 3) and (self.board.state - move >= 0))

    def check_for_winner(self, move, player, opponent) -> TakeawayPlayer:
        """
        Checks to see if someone has won the game.

        Parameters:
            move (int): The proposed move to check the legality of
            player (TakeawayPlayer): The player making the current move
            opponent (TakeawayPlayer): The current opponent of the turn

        Returns:
            The winning player, if applicable, else None
        """
        winner = None
        if move == 0 or move is None:
            winner = opponent
        elif self.board.state == 0:
            winner = player

        # Only assign winner if winner was found
        if winner is not None:
            self.board.summary.winner = winner.player_name

        return winner
