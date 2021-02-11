##
# A function to write Toothpick Takeaway game data to a .csv file.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: Nov 30, 2020
##

import csv

def write_to_csv(game_data, filename):
    """
    Writes game data to a .csv file.

    Parameters:
        game_data (list): Data of each turn made in the game and the winner of that game
        filename (string): Name of the file to write to
    """
    # Get the total number of toothpicks at the start
    start_val = max(game_data[0].history.keys())

    # Make a descending list of all toothpicks left
    toothpicks_left = list(range(start_val, 0, -1))

    # Create our headings: Toothpicks left and turn
    headings = []
    for heading in toothpicks_left:
        headings.append(heading)
        headings.append("turn_{}".format(heading))
    headings.append("winner")

    # Start building rows; one row per game
    rows = []
    for summary in game_data:
        # How many toothpicks were taken at each turn in the game
        turns = [summary.history[turn]["move"] for turn in summary.history]
        # Who took those toothpicks
        names = [summary.history[turn]["name"] for turn in summary.history]

        # Start creating a row
        moves = []
        for i in range(len(turns)):
            # Append the toothpicks taken
            moves.append(turns[i])
            # Append the player who took them
            moves.append(names[i])

            # If a turn was 2, add a turn of 0 after it
            # This ensures that our rows are all the same length
            if turns[i] == 2:
                moves.append(None)
                moves.append(None)

        # Append the winner of the game
        moves.append(summary.winner)

        # Add the row we just made to the running list of rows
        rows.append(moves)

    # Write to csv
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headings)
        csvwriter.writerows(rows)
