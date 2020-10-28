##
# This class models a Referee for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Sep 22, 2020
##
class Referee:

    def __init__(self, board, legal_function = lambda x: None,
                 winning_function = lambda x: None):
        """ This class models a referee for a game.
        Args:
            board : The board of the game being played``

        """
        self.is_game_over = False
        self.board = board
        self.is_legal = legal_function
        self.is_winning = winning_function

    def update_board(self, board, player, other_player) -> object:
        """ This method will handle updating the game board.

        Args:
            board : the game board
            player : the current player making the move
            other_player : the player not making the move

        Return:
            The winning_player or None depending on the move update

        """
        current_move = self.ask_for_move(board, player, None)
        prev_move_list = []
        is_turn_over = False
        winning_player = None

        while not is_turn_over:
            current_move = player.move(board)

            # check to see if player has given up
            if current_move in prev_move_list or current_move is None:
                is_turn_over = True
                self.is_game_over = True
                winning_player = other_player

            elif not(self.is_legal(board, current_move)):
                prev_move_list.append(current_move)
                #is_turn_over = True

        return winning_player

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
            elif not self.is_legal(self.board.state, proposed_move):
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
