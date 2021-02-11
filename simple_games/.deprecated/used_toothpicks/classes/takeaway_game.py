##
# This implements a Game that takes a list/set of players, a referee, and a
# board. It automates the process of playing the game, and returns a winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Oct 17, 2020
##

from takeaway_data import TakeawayData

class TakeawayGame:
    def __init__(self, board, referee, players):
        """
        Instantiates a new TakeawayGame object.

        Parameters:
            board (TakeawayBoard): The board being played on
            referee (TakeawayReferee): The referee for the game
            players (list): The players playing the game

        Returns:
            A newly instatiated TakeawayGame
        """
        self.referee = referee
        self.board = board
        self.players = players

    def play(self,narrated = False) -> TakeawayData:
        """
        Plays a single game of Toothpick Takeaway.

        Parameters:
            narrated (bool): Whether to narrate the game

        Returns:
            The winner of the game and the move history
        """
        self.board.reset()
        turn = 0
        winner = None

        while winner is None:
            player = self.players[turn % 2]
            opponent = self.players[(turn + 1) % 2]
            turn = turn + 1

            move = self.referee.update(player)
            winner = self.referee.check_for_winner(move, player, opponent)

            if (narrated):
                print(player.player_name, "drew", move, "toothpicks.", self.board.state, "left")

        return self.board.summary
