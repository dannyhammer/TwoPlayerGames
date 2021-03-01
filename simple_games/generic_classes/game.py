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
        self.players = players

    def play(self, narrated = False):
        """
        Plays a game on the current board, moderated by the referee, with the
        two players provided.

        Args:
            narrated : Whether to enable debug-friendly narration in the game

        Return:
            The game board being played on
        """

        # Reset the board for additional playthroughs
        self.board.reset()

        # Keep a turn counter for assigning current player
        turn = 0
        player = self.players[turn]
        opponent = self.players[turn + 1]

        winner = None
        while not self.referee.is_game_over(self.board):

            # Request a move from the current player
            move = self.referee.ask_for_move(player, self.board)

            if narrated:
                print("{} -> {}".format(player.name, move))

            # If the move is NOT valid, exit the loop, as the game is over
            # The current opponent is also declared the winner
            if move is None:
                winner = opponent
                break

            # Tell the referee to update the board with the (valid) move
            else:
                self.referee.update_board(self.board, player, move)

            # Next turn
            opponent = self.players[turn]
            turn = (turn + 1) % 2
            player = self.players[turn]

        # Declare a winner using the game's rules and board
        # If either player made an illegal move, the winner has already been
        # decided and this function just updates the board's history
        winner = self.referee.declare_winner(self.board, self.players, winner)

        if narrated:
            print("Winner: " + str(winner.name))

        return self.board
