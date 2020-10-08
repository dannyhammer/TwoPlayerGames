
##
# This implements a Game that takes a list/set of players, a referee, and a
# board. It automates the process of playing the game, and returns a winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Oct 7, 2020
##


class TakeawayGame:
    def __init__(self, board = None, referee = None, players = None):
        """ The game constructor declares a new board, referee, and two
        players.

        Args:
            board : The game board
            referee : The current game referee
            players : A list of the players

        """
        self.referee = referee
        self.board = board
        self.players = players

    def play(self):
        """ This function allows for the game to be played.

        Args:
            None

        Return:
            The wining player
        """

        turn = 0
        winner = None
        while winner is None:
            # Set the current player
            current_player, opponent = self.get_players_at_turn(self.players, turn)
            turn = (turn + 1) % 2

            winner, move = self.referee.ask_for_move(self.board, current_player, opponent)

            # If a winner was not found, update the board
            if winner is None:
                self.board = self.referee.update_board(move, self.board)
                #print("\tPlayer", current_player.player_num, "drew", move, "toothpicks")

                #print("\t\t", self.board.state, "toothpicks left")

        return winner

    def get_players_at_turn(self, players, turn):
        """ Gets each player at the end of a turn

        Args:
            players : The players in the game
            turn : Which player's turn it is (0 for 1, 1 for 2)

        Return:
            The player whose turn it is and the opposing player
        """
        current_player = players[turn]
        turn = (turn + 1) % 2
        opponent = players[turn]

        return current_player, opponent
