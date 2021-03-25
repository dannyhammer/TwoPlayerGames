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

    def __init__(self, ruleset, min_games, fitness):
        """
        Constructs a new, empty tournament

        Args:
            ruleset : The ruleset of the game in the tournament
            min_games : Minimal number of games each player must compete in during a tournament
            fitness : Initial fitness needed for a player to survive
        """
        self.ruleset = ruleset
        self.min_games = min_games
        self.fitness = fitness
        self.trials = 0
        self.board = b.Board(ruleset.initial_state, ruleset.bounds)
        self.referee = r.Referee(self.board, ruleset)


    def compete(self, p1_pop, p2_pop):
        """
        Places all players in a ranked tournament against each other
        to determine the best players.

        Args:
            p1_pop : Player 1 population to compete in the tournament
            p2_pop : Player 2 population to compete in the tournament

        Return:
            Two lists, each containing the "best" Player 1s and Player 2s, respectively
        """
        # Create lists to hold the "best" players
        best_p1s = self.eliminate(p1_pop, p2_pop, True)
        best_p2s = self.eliminate(p2_pop, p1_pop, False)

        return sorted(best_p1s, reverse=True), sorted(best_p2s, reverse=True)

    def eliminate(self, player_pop, opponent_pop, player_is_p1):
        """
        Competes all players against a random sample of opponents and eliminates
        players who do not meet the fitness criteria.

        Args:
            player_pop : Population of players to compete
            opponent_pop : Population of opponents to sample from
            player_is_p1 : Whether the `player_pop` is a Player 1 population

        Return:
            A list of the "elite" players who passed the fitness criteria.
        """
        # Create a list of elite/best players
        elite = []

        for player in player_pop:
            # Get a random sample of opponents
            # The sample should be the smaller of the two:
            #   - Number of opponents available
            #   - The minimum games specified
            opponent_sample = sample(opponent_pop, min(len(opponent_pop), self.min_games))

            # Every player must play every opponent in the sample
            for opponent in opponent_sample:
                # Order the players based on p1/p2 status
                players = [player, opponent] if player_is_p1 else [opponent, player]

                # Create and play the game
                game = g.Game(self.referee, self.board, players)

                # At present, we don't need this data, so we throw it away
                _ = game.play()

            # Only append players whose fitness at least the threshold
            if player.fitness() >= self.fitness:
                elite.append(player)

        return elite
