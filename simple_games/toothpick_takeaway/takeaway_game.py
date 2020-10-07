
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


# TODO: initialize
# should take as input a board, a player_list, a referee, and a first player
# if no first player given, make it be the first player in the list.


    def play(self):
        """ This function allows for the game to be played.

        Args:
            None

        Return:
            The wining player
        """

        # This code serves as a general example of how a 'play()' function would work
        """
        current_player = None
        game_over = False
        while(not(game_over)):
            # select a player move based on state of board
            player_move = current_player.move(board.state)
            # check to see if move is legal
            if self.referee.is_legal(player_move, board.state):
                next_player, new_state = self.board.update(
                    current_player, player_move, board.state)  # update board if legal
                # check to see if move has won
                if self.referee.is_winning(self.board.state):
                    winning_player = current_player  # set winning_player and return if needed
                    return winning_player
                else:  # if no one won, update current player and board
                    board.state = new_state
                    current_player = next_player
        """

        # Establish a current player and start the loop
        current_player = 0
        game_over = False
        while not(game_over):
            # Update the current player
            current_player = ((current_player + 1) % 2) + 1
