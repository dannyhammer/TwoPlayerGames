import referee
import player
import board


class Game:
    """
    This implements a Game that takes a list/set of players, a referee, and a board.
    It automates the process of playing the game, and returns a winner.

    TODO: Finish Docstring for methods and other attributes.
    """

    def __init__(self):
        self.referee = Referee()
        self.board = Board()
        self.players = [Player(1), Player(2)]


# TODO: initialize
# should take as input a board, a player_list, a referee, and a first player
# if no first player given, make it be the first player in the list.


    def play(self):
        """
        TODO: Docstring
        """
        game_over = False
        while(not(game_over)):
            # select a player move based on state of board
            player_move = current_player.move(board.state)
            # check to see if move is legal
            if referee.is_legal(player_move, board.state):
                next_player, new_state = board.update(
                    current_player, player_move, board.state)  # update board if legal
                   # check to see if move has won
                   if referee.is_winning(board.state):
                        winning_player = current_player  # set winning_player and return if needed
                        return winning_player
                    else:  # if no one won, update current player and board
                        board.state = new_state
                        current_player = next_player
