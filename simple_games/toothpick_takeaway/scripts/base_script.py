import sys, os
sys.path.append(os.path.abspath("../classes/"))

from takeaway_board import TakeawayBoard
from takeaway_referee import TakeawayReferee
from takeaway_game import TakeawayGame
from takeaway_player import TakeawayPlayer
from takeaway_strategies import TakeawayStrategy
from csv_writer import write_to_csv

def run_game(num_games, toothpicks, p1_strat_name, p2_strat_name, display_output = False):
    """
    Runs a specified number of games.

    Parameters:
        num_games (int): Number of games to run
        toothpicks (int): Initial number of toothpicks to use
        p1_strat_name (string): Name of strategy for player 1 to use
        p2_strat_name (string): Name of strategy for player 2 to use
        display_output (bool): Whether to display output to the console
    """
    # Obtain the strategies for each player
    p1_strategy = TakeawayStrategy(p1_strat_name)
    p2_strategy = TakeawayStrategy(p2_strat_name)

    # We're going to collect a lot of data
    game_data = []

    # Create a board of toothpicks
    board = TakeawayBoard(toothpicks)
    # Create a referee to govern the board
    referee = TakeawayReferee(board)

    # Create two players; each with a unique strategy
    player_1 = TakeawayPlayer(player_name = "player_1", strategy = p1_strategy)
    player_2 = TakeawayPlayer(player_name = "player_2", strategy = p2_strategy)

    for _ in range(num_games):
        # Create the game
        game = TakeawayGame(board, referee, [player_1, player_2])

        # Play the game
        summary = game.play(narrated = False)
        game_data.append(summary)

    if display_output:
        for summary in game_data:
            print()
            for turn in summary.history:
                print(turn, summary.history[turn])
            print("WINNER: ", summary.winner)

    # Write to csv
    filename = "{}_{}_{}.csv".format(p1_strat_name, p2_strat_name, num_games)
    write_to_csv(game_data, filename)
