##
# This class models a Referee for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Sep 22, 2020
##
class TakeawayReferee:

    def __init__(self, board):
        """ This class models a referee for a game.
        Args:
            board : The board of the game being played``

        """
        self.is_game_over = False
        self.board = board

    def update_board(self, board, player, other_player) -> object:
        """ This method will handle updating the game board.

        Args:
            board : the game board
            player : the current player making the move
            other_player : the player not making the move

        Return:
            The winning_player or None depending on the move update

        """
        winning_player, current_move = self.ask_for_move(board, player, other_player)
        board.move_history[board.state] = {"name": player.player_name,
                                               "move":current_move }
        if (winning_player is None):
            board.state = board.state - current_move


        return winning_player, current_move

    def ask_for_move(self, board, player, opponent):
        """ This method takes in the board and current player and prompts for
        the next move.

        Then returns the move and a winner if found

        Args:
            board : the game board
            player : player whose turn it is
            opponent: player whose turn it is not

        Return:
            The winning player, if applicable
            The players move
        """
        previous_moves_tried = [] #to check for repeats
        is_turn_over = False
        winner = None

        while not is_turn_over:
            #see what move the player would want to make.
            proposed_move = player.move(board)

            #check to see if player has given up
            if (proposed_move in previous_moves_tried) or (proposed_move is None): 
                winner = opponent
                is_turn_over = True
                proposed_move = None

            #no change in is_turn_over, so we should re-enter the while loop
            elif not self.is_legal(board, proposed_move):
                previous_moves_tried.append(proposed_move)

            #check to see if player won
            elif self.is_winning(board, proposed_move):
                winner = player
                is_turn_over = True

            #in this case the move is legal and not winning
            else:
                winner = None
                is_turn_over = True

        return winner, proposed_move


    def is_legal(self, board, move) -> bool:
        """ This function allows for the referee object to check if a move is
        valid.

        Args:
            board : the current board
            move  : the current move being made 

        Return:
            boolean : True or False depending on the move validity
        """
        return ((move > 0) and (move < 3) and (board.state - move >= 0))


    def is_winning(self, board, move) -> bool:
        """A method to check if the current player is winning at a given 
        instance of the game.

        Args:
            board : the game board
            move : the current move

        Return:
            True or False based on the 'win condition'
        """
        return (board.state - move) == 0
