from random import choice

def random_move(board):
    """ Chooses a random legal move

    Args:
        board : the game board to move on

    Returns:
        A random move to try
    """
    move_selected = False
    possible_moves = [1,2]
    moves_tried = []

    while not(move_selected):
        # Get a random move
        move_to_try = choice(possible_moves)

        # If the move is not legal, mark it as tried
        if (board.state - move_to_try) < 0:
            moves_tried.append(move_to_try)
        else:
            move_selected = True

        # If all moves have been tried, return None
        if set(moves_tried) == set(possible_moves):
            return None

        return move_to_try

def always_take_one(board):
    """ Always take one toothpick

    Args:
        board : the game board to move on

    Returns:
        1 if possible, else None
    """
    # Check for legality
    if (int(board.state) - 1) < 0:
        return None
    else:
        return 1

def always_take_two(board):
    """ Always take two toothpicks

    Args:
        board : the game board to move on

    Returns:
        2 if possible, else None
    """
    # Check for legality
    if (int(board.state) - 2) < 0:
        return None
    else:
        return 2

def human(board):
    """ Prompts the user to input

    Args:
        board : the game board to move on

    Returns:
        A user-entered move
    """
    return int(input("Please make your move > "))

strategies = {"human": human,
              "random": random_move,
              "random_move": random_move,
              "take_one": always_take_one,
              "take_two": always_take_two,
              "always_take_one": always_take_one,
              "always_take_two": always_take_two}
