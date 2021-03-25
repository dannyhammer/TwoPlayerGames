##
# This class contains functions to conduct a tournament between populations
# of players.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-03-06
##
from random import sample 
from . import board as b
from . import referee as r
from . import game as g

class Tournament:

    def __init__(self):
        """
        Constructs a new, empty tournament
        """
        self.trials = 0


    def compete(self, p1_pop, p2_pop, ruleset, num_games = 10, fitness = 0.8):
        """
        Places all players in a ranked tournament against each other
        to determine the best players.

        Args:
            p1_pop : Player 1 population to compete in the tournament
            p2_pop : Player 2 population to compete in the tournament
            ruleset : Ruleset of the game being played
            num_games : (Optional) The number of games for each player to play
            fitness : (Optional) Percentage of wins players need to be considered "good"

        Return:
            Two lists, each containing the "best" Player 1s and Player 2s, respectively
        """
        board = b.Board(ruleset.initial_state, ruleset.bounds)

        ref = r.Referee(board, ruleset)

        # Create lists to hold the "best" players
        best_p1s = self.eliminate(p1_pop, p2_pop, num_games, ref, board, fitness, True)
        best_p2s = self.eliminate(p2_pop, p1_pop, num_games, ref, board, fitness, False)

        return sorted(best_p1s, reverse=True), sorted(best_p2s, reverse=True)

    def eliminate(self, player_pop, opponent_pop, num_games, referee, board, fitness, player_is_p1):
        """
        Competes all players against a random sample of opponents and eliminates
        players who do not meet the fitness critera.

        Args:
            player_pop : Population of players to compete
            opponent_pop : Population of opponents to sample from
            num_games : Number of games to play
            referee : Referee of the game
            board : Board being played on
            fitness : Win percentage required to survive
            player_is_p1 : Whether the `player_pop` is a Player 1 population
        """
        # Create a list of elite/best players
        elite = []

        for player in player_pop:
            # Get a random sample of opponents
            opponent_sample = sample(opponent_pop, min(len(opponent_pop), num_games))

            # Every player must play every opponent in the sample
            for opponent in opponent_sample:
                # Order the players based on p1/p2 status
                players = [player, opponent] if player_is_p1 else [opponent, player]

                # Create and play the game
                game = g.Game(referee, board, players)
                board = game.play()

            # Only append players whose fitness at least the threshold
            if player.fitness() >= fitness:
                elite.append(player)

        return elite
