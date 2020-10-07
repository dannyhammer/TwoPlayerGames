# Unbalanced Rook Protype
# Daniel Hammer
# 2020-10-01

import random

# Board size
SIZE = 5

"""
IMPORTANT NOTE: This is NOT finished by any means. This is just a prototype.
I will add docstrings where needed.

This code exists simply to illustrate a concrete example of Unbalanced Rook.
We will use this code to abstract out into generic game classes.
This is NOT optimized, at all. It is a proof of concepts.
Many things need to be changed (like SIZE becoming a field of the board)
"""


def main():
    """
    Unbalanced Rook game
    """

    # Make two players
    p1 = make_player("Human")
    p2 = make_player("Computer")
    players = [p1, p2]

    # Make a board and start the game
    board = make_board(SIZE)
    board[0][0] = True

    # Initialize turn counter
    turn_counter = 0

    # Show the game start
    print_board(board)

    # Constantly check if the game is over
    while not is_game_over(board):
        # Get the current player
        current_player = players[turn_counter]

        # Get the direction and number of spaces to move
        direction, spaces = get_move(current_player, board)

        # Move the rook
        board = move(board, direction, spaces)

        # Display the move
        print(current_player["name"], "moved", spaces, direction)

        # Increment the turn counter
        turn_counter = (turn_counter + 1) % 2

        print_board(board)

    print("Game over, " + str(current_player["name"]) + " wins!")


def move(board, direction, spaces):
    """
    Actually move the rook
    """

    # Get the current rook position
    i, j = get_current_pos(board)

    # Set the position to false, as the rook will be moving
    board[i][j] = False

    # Increment the distance according to direction
    if direction == "right":
        board[i][j + spaces] = True

    if direction == "down":
        board[i + spaces][j] = True

    # We have to update the board by returning a new version of it
    return board


def get_move(player, board):
    """
    Gets the direction and number of spaces to move the rook
    """

    direction = ""
    spaces = -1

    # If human player, get input
    if player["name"] == "Human":
        # Obtain a valid right/down direction
        while direction != "right" and direction != "down":
            direction = str(
                input("Enter a direction (right or down): ")).lower()

            # Make the player choose again if they attempt to go into a wall
            if get_max_distance(board, direction) < 1:
                direction = ""

        # Obtain a valid number of spaces to move
        while spaces < 1 or spaces > get_max_distance(board, direction):
            spaces = int(
                input("Enter the number of spaces you wish to move " + str(direction) + ": "))

    # If computer player, get random choice
    if player["name"] == "Computer":
        # Ensure that the computer does not try to go right or down when against a wall
        while get_max_distance(board, direction) < 1:
            direction = random.choice(["right", "down"])

        spaces = random.randint(1, get_max_distance(board, direction))

    return (direction, spaces)


def get_max_distance(board, direction):
    """
    Gets the maximum distance the rook can travel
    """
    current_position = get_current_pos(board)
    max_distance = 0

    if direction == "right":
        max_distance = SIZE - current_position[1] - 1

    if direction == "down":
        max_distance = SIZE - current_position[0] - 1

    return max_distance


def get_current_pos(board):
    """
    Gets the current (i, j) position of the rook
    """
    current_position = (0, 0)

    # Loop through the board
    for i in range(SIZE):
        for j in range(SIZE):

            # If the current index is True, update the current position
            if board[i][j]:
                current_position = (i, j)

    return current_position


def is_game_over(board):
    """
    If the (n x n)th position is true, the rook has arrived at a terminal state
    """
    return board[SIZE - 1][SIZE - 1]


def make_board(size):
    """
    Returns a size * size board of False
    """
    board = [[False for i in range(size)] for j in range(size)]

    return board


def make_player(name):
    """
    Mock constructor to make a player
    """
    player = {"name": name}
    return player


def print_board(board):
    """
    Just prints the board, formatted nicely. Not actually needed for final product
    """
    print("\n\tBOARD")
    for i in range(SIZE):
        print("\t", end="")
        for j in range(SIZE):
            c = "X" if board[i][j] else "O"
            print(c, end=" ")
        print()


if __name__ == "__main__":
    main()
