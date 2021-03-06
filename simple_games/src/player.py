##
# This class models a player for a game.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-02-06
##
class Player:

    def __init__(self, name, strategy):
        """
        The player constructor.

        Args:
            name: The player's label
            strategy: A strategy function used by the player
        """
        self.name = name
        self.strategy = strategy
        self.generation = 0
        self.wins = 0
        self.losses = 0

    def move(self, board):
        """
        This function takes in a board and then allows the player to make a
        choice on the next move.

        Args:
            board : The board object for the current game

        Return:
            The move made.
        """
        return self.strategy.move(board)

    def fitness(self):
        """
        Computes the fitness (win percentage) of the player.
        If the player has played no games, the fitness is 0.0.

        Return:
            The fitness (win percentage) of the player
        """
        total_games = self.wins + self.losses
        # Account for dividing by zero
        return float(self.wins) / float(total_games) if total_games else 0.0


    def __str__(self):
        """
        Overrides the default implementation of `str()`.
        Provides a more readable way of printing players.

        Return:
            A formatted string containing the player's name and strategy's info
        """
        string = "{}: {}".format(self.name, self.strategy.name)

        # If strategy data is available, display it
        if self.strategy.data:
            string = "{}: {}".format(string, self.strategy.data)
        string = "{}\nGen: {} Wins: {} Losses: {}".format(string,
                self.generation, self.wins, self.losses)

        return string

    def __eq__(self, other):
        """
        Overrides the default implementation of `==`.
        Provides a way of comparing players.

        Args:
            other : The player being compared with

        Return:
            True if the players are equal, else False
        """
        if isinstance(other, Player):
            return (self.strategy is other.strategy
                    and self.name is other.name
                    and self.wins == other.wins
                    and self.losses == other.losses
                    and self.generation == other.generation)

        return False

    def __ne__(self, other):
        """
        Overrides the default implementation of `!=`.
        Provides a way of comparing players.

        Args:
            other : The player being compared with

        Return:
            True if the players are not equal, else False
        """
        if isinstance(other, Player):
            return (self.strategy is not other.strategy
                    or self.name is not other.name
                    or self.wins != other.wins
                    or self.losses != other.losses
                    or self.generation != other.generation)

        return False

    def __lt__(self, other):
        """
        Overrides the default implementation of `<`.
        Provides a way of comparing players.

        Args:
            other : The player being compared with

        Return:
            True if `self` has higher fitness than `other`, else False
        """
        if isinstance(other, Player):
            return self.fitness() < other.fitness()

        return False

    def __le__(self, other):
        """
        Overrides the default implementation of `<=`.
        Provides a way of comparing players.

        Args:
            other : The player being compared with

        Return:
            True if `self` has lower or equal fitness to `other`, else False
        """
        if isinstance(other, Player):
            return self.fitness() <= other.fitness()

        return False

    def __gt__(self, other):
        """
        Overrides the default implementation of `>=`.
        Provides a way of comparing players.

        Args:
            other : The player being compared with

        Return:
            True if `self` has higher fitness than `other`, else False
        """
        if isinstance(other, Player):
            return self.fitness() > other.fitness()

        return False

    def __ge__(self, other):
        """
        Overrides the default implementation of `>=`.
        Provides a way of comparing players.

        Args:
            other : The player being compared with

        Return:
            True if `self` has higher or equal fitness to `other`, else False
        """
        if isinstance(other, Player):
            return self.fitness() >= other.fitness()

        return False
