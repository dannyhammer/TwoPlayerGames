##
# This implements a Game that takes a list/set of players, a referee, and a
# board. It automates the process of playing the game, and returns a winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##
class Game:

    def __init__(self, referee, board, players):
        """
        Creates a new game with the given referee, board, and players.

        Args:
            referee : The current game referee
            board : The game board
            players : A list of two players
        """
        self.referee = referee
        self.board = board
        self.player = players[0]
        self.opponent = players[1]

    def play(self):
        """
        Plays a game on the current board, moderated by the referee, with the
        two players provided.

        Return:
            The game board being played on
        """
        winner = None
        while winner is None:

            # Request a move from the current player
            move = self.referee.ask_for_move(self.player, self.board)

            # If the move is NOT valid, exit the loop
            if move is None:
                winner = self.opponent

            # Tell the referee to update the board with the (valid) move
            else:
                self.referee.update_board(self.board, self.player, move)

            # Check if the game has been won
            if self.referee.is_game_over(self.board):
                winner = self.player

            # Next turn
            self.player, self.opponent = self.opponent, self.player

        # Declare a winner to the game
        self.referee.declare_winner(self.board, winner)
        return self.board
