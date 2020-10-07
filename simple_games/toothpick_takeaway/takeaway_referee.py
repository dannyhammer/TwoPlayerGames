##
# This class models a Referee for the toothpick takeaway game.
#
# Authors: Daniel Hammer, Nihcolas O'Kelley, Andrew Shelton

#
##

class takeaway_referee(Referee):
    """The toothpick takeaway referee subclass."""

    def __init__(self):
        """ This class models a referee for a game.
        Args:
            none

        """
        Referee.__init__(self)

    def update_board(self, board, player, other_player) -> object:
        """ This method will handle updating the game board.

        Args:
            board : the game board
            player : the current player making the move
            other_player : the player not making the move

        Return:
            The winning_player or None depending on the move update

        """
        current_move = self.ask_for_move(board, player)
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

    def ask_for_move(self, board, player) -> str:
        """ This method takes in the board and current player and prompts for
        the next move.

        Then returns the move.

        Args:
            board : the game board
            player : player that is being prompted

        Return:
            The players move
        """
        # Gather all the moves left
        available_moves = board.possible_moves()

        available_moves_as_str = list(map(str, board.possible_moves()))

        while True:
            player_move = input("Enter your move >").rstrip()

            if player_move == 'show moves':
                print("Available Moves: " + "\n".join(
                    ["#%d: %s" % (i+1, m)
                     for i, m in enumerate(available_moves)]
                ) + "\n")

            elif player_move == 'quit':
                player_move = "Quit"
                raise KeyboardInterrupt

            elif str(player_move) in available_moves_as_str:
                return [available_moves[available_moves_as_str.index(str(player_move))]]
        return player_move

    def is_legal(self, board_state, move) -> bool:
        """ This function allows for the referee object to check if a move is
        valid.

        Args:
            board_state : the state of the board
            move  : the current move being made 

        Return:
            boolean : True or False depending on the move validity
        """
        pass

    def is_winning(self, board, move) -> bool:
        """A method to check if the current player is winning at a given 
        instance of the game.

        Args:
            board : the game board
            move : the current move

        Return:
            True or False based on the 'win condition'
        """
        pass
