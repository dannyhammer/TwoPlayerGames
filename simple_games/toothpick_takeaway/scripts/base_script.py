import sys, os
sys.path.append(os.path.abspath("../classes/"))

from takeaway_board import TakeawayBoard
from takeaway_referee import TakeawayReferee
from takeaway_game import TakeawayGame
from takeaway_player import TakeawayPlayer
from takeaway_strategies import strategies

def run_game(num_games, board_sizes, p1_strat_name, p2_strat_name):
    """
    Runs a game and converts the game data to a csv.

    Args:
        num_games (int) : The number of games to run
        board_sizes (list) : A list of board sizes ro run `num_games` on
        p1_strat_name (string) : The name of a `takeaway_strategy` for player 1
        p2_strat_name (string) : The name of a `takeaway_strategy` for player 2
    """

    # Obtain the strategies for each player
    p1_strategy = strategies[p1_strat_name]
    p2_strategy = strategies[p2_strat_name]

    # We're going to collect a lot of data
    game_data = []

    # Run a set number of games for each board
    for toothpicks in board_sizes:
        # Create a board of toothpicks
        my_board = TakeawayBoard(toothpicks)
        # Create a referee to govern the board
        my_referee = TakeawayReferee(my_board)

        # Create two players; each with a unique strategy
        player_1 = TakeawayPlayer(player_name = "player_1", strategy = p1_strategy)
        player_2 = TakeawayPlayer(player_name = "player_2", strategy = p2_strategy)

        for _ in range(num_games):
            # Create the game
            my_game = TakeawayGame(board = my_board,
                                   referee = my_referee,
                                   players = [player_1, player_2])

            # Play the game
            winner, history = my_game.play(narrated = False)
            game_data.append((winner.player_name, history))

    # Write to csv
    from csv_writer import write_to_csv
    filename = "{}_{}_{}.csv".format(p1_strat_name, p2_strat_name, num_games)
    write_to_csv(game_data, filename)

    # Move the file
    import shutil
    shutil.move(filename, "../data_files/{}".format(filename))
