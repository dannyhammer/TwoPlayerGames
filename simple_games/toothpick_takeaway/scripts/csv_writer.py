def write_to_csv(game_data, filename):
    # Get the total number of toothpicks at the start
    start_val = max(game_data[0][1])
    # Make a descending list of all toothpicks left
    toothpicks_left = list(range(start_val, 0, -1))

    # Create our headings
    headings = []
    for heading in toothpicks_left:
        # Number of toothpicks left
        headings.append(heading)
        # Whose turn it was when those toothpicks were taken
        headings.append("turn_{}".format(heading))
    # Append the winner column
    headings.append("winner")

    # Start building rows; one row per game
    rows = []
    for game in game_data:
        winner, history = game

        # How many toothpicks were taken at each turn in the game
        turns = [turn["move"] for turn in history.values()]
        # Who took those toothpicks
        names = [state["name"] for state in history.values()]

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
                moves.append(0)
                moves.append(None)

        # Append the winner of the game
        moves.append(winner)

        # Add the row we just made to the running list of rows
        rows.append(moves)

    # Write to csv
    import csv
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headings)
        csvwriter.writerows(rows)
