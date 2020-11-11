
##
# This implements a Game that takes a list/set of players, a referee, and a
# board. It automates the process of playing the game, and returns a winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Oct 17, 2020
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

    def play(self,narrated = False):
        """ This function allows for the game to be played.

        Args:
            verbose (boolean): Whether or not status should be printed. 

        Return:
            The winning player
        """
        self.board.reset()
        turn = 0
        winner = None
        game_on = True

        while game_on:
            current_player = self.players[turn % 2]
            current_opponent = self.players[(turn + 1) % 2]
            turn = turn + 1

            winner, current_move = self.referee.update_board(board = self.board, player = current_player, opponent = current_opponent)
            game_on = (winner is None)

            if (narrated):
                print(current_player.player_name, "drew", 
                          current_move, "toothpicks")
                print(self.board.state, "toothpicks left")

        return winner, self.board.move_history
