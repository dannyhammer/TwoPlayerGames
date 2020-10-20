import referee
import player
import board

##
# This implements a Game that takes a list/set of players, a referee, and a
# board. It automates the process of playing the game, and returns a winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Sep 22, 2020
##


class Game:
    def __init__(self,game_referee = referee.Referee(), game_board = board.Board(),
        players = [player.Player(), player.Player()]):
        """The game constructor declares a new board, referee, and two
        players. First player should be listed first. 

        Args:
            referee : the current game referee
            board : the game board
            players : the list of players
        """
        self.game_referee = game_referee
        self.game_board = game_board
        self.players = players


    def play(self):
        """ This function allows for the game to be played.

        Args:
            None

        Return:
            winner (player_name): the name of the player who won the game 
        """
        
        current_player = players[0]
        other_player = players[1]
        winner = None 
        
        while(winner is None):
            winner, proposed_move = self.referee.ask_for_move(self.game_board, 
                                                                        self.current_player,
                                                                        self.other_player)
            current_board, current_player = self.referee.update(self.game_board,
                                                                          self.current_player,
                                                                          proposed_move)
            
        return winner
                                                                          
        
        
