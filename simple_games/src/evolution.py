##
# This class contains the functions needed to generate populations, breed players,
# and generate mutations during reproduction.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-03-06
##

from random import sample, random, randrange
from copy import deepcopy
from . import tournament as t
from . import player as p

class Evolution:

    def __init__(self, strategy, mutation_rate = 0.025):
        """
        Creates a new Evolution object.

        Args:
            strategy : Baseline strategy to begin evolving from
            mutation_rate : (Optional) Chance that a mutation will occur during reproduction
        """
        self.strategy = strategy
        self.mutation_rate = mutation_rate
        self.tournament = t.Tournament()

    def generate_population(self, num_players, player_to_gen):
        """
        Generates a population of players with random strategies for the
        Graph Coloring Game.

        Args:
            num_players : The number of players to create
            player_to_gen : 1 or 2, depending on what population we are generating

        Return:
            A list of players with random strategies
        """
        # A list to hold the strategies
        strategies = []
        generated = 0
        failures = 0
        max_attempts = 10 * num_players

        while generated < num_players:
            # Clone the example strategy
            strat = deepcopy(self.strategy)

            # Shuffle the orderings in the data
            new_data = {}
            for key in strat.data.keys():
                new_data[key] = sample(strat.data[key], len(strat.data[key]))

            # Update the data of the new strategy
            strat.set_data(new_data)

            # Only append unique strategies
            if strat not in strategies:
                strategies.append(strat)
                generated += 1
            else:
                failures += 1

            # Exit if it is taking too long to create players
            if failures >= max_attempts:
                print("Error: Failed to create unique players {} times. Aborting".format(failures))
                break

        # A list to hold the players
        players = []
        # Generate a new player for every strategy
        for strat in strategies:
            player = p.Player("Player {}".format(player_to_gen), strat)
            # Strategies are unique, so we don't need to check player uniqueness
            players.append(player)
            generated += 1

        return players

    def spawn(self, parent1, parent2, child_name, child_strat_name, mutation_rate = .0025):
        """
        Spawns a new `Player` instance using the provided players
        as parents.

        Args:
            parent1 : The first parent
            parent2 : The second parent
            child_name : The name of the child-to-be
            child_strat_name : The name of the child's strategy
            mutation_rate : Percentage for a mutation to occur

        Return:
            A new `Player` with traits from both parents
        """
        # Get all the data 
        traits = parent1.strategy.data.keys()

        child_traits = {}
        for trait in traits:
            # Obtain the current trait from both parents
            p1_trait = parent1.strategy.data[trait]
            p2_trait = parent2.strategy.data[trait]

            # Randomly generated crossover point
            crossover = randrange(0, len(p1_trait))

            # Choose up to the crossover from parent 1
            p1_inherit = p1_trait[:crossover]

            # Choose the rest of the genes from parent 2
            p2_inherit = [gene for gene in p2_trait if gene not in p1_inherit]

            # Assemble child's trait
            child_trait = p1_inherit + p2_inherit

            # Mutation Check: If mutation occurs, swap two genes
            if random() < mutation_rate:
                index1, index2 = sample(range(len(p1_trait)), 2)
                child_trait[index1], child_trait[index2] = child_trait[index2], child_trait[index1]

            # Construct the child's traits
            child_traits[trait] = child_trait

        child_strat = deepcopy(parent1.strategy)
        child_strat.set_name(child_strat_name)
        child_strat.set_data(child_traits)

        child = p.Player(child_name, child_strat)
        child.generation = max(parent1.generation, parent2.generation) + 1

        return child

    def evolve(self, pop_size, ruleset, iterations, num_games = 10, mutation_rate = 0.025, fitness = 0.5, max_fitness = 0.9, fitness_increment = 0.05, verbose = False):
        """
        Generates random populations of players and evolves them across a specified
        number of generations.
        Evolution is composed of competing players, eliminating poor performers,
        and reproducing good players with each other to produce optimal children.

        Args:
            pop_size : Size of the populations to generate
            ruleset : The ruleset of the game to play on
            iterations: Number of iterations to evolve players
            num_games : (Optional) Minimum number of games each player must play per generation
            mutation_rate : (Optional) Percentage to mutation to occur
            initial_fitness : (Optional) Initial minimum win percentage to continue playing
            max_fitness : (Optional) Maximum fitness to test players against
            fitness_increment : (Optional) What to increment the fitness by after each iteration
            verbose : (Optional) Whether to print debug information

        Return:
            Two lists, containing the elite P1 and P2 populations, respectively
        """
        # Create populations of players with random strategies
        p1_pop = self.generate_population(pop_size, 1)
        p2_pop = self.generate_population(pop_size, 2)

        for i in range(iterations):
            # Compete both populations against each other
            p1_pop, p2_pop = self.tournament.compete(p1_pop, p2_pop, ruleset, num_games, fitness)

            if verbose:
                print("\nITERATION: {}, FITNESS: {}".format(i, round(fitness, 4)))
                print("\tP1 Pop: " + str(len(p1_pop)))
                print("\tP2 Pop: " + str(len(p2_pop)))

            # Repopulate p1_pop
            self.repopulate(p1_pop, pop_size, 1, i, ruleset, mutation_rate, verbose)
            self.repopulate(p2_pop, pop_size, 2, i, ruleset, mutation_rate, verbose)

            # Never increase fitness beyond 90%
            if fitness < max_fitness:
                fitness += fitness_increment

        # Return the elite players
        return p1_pop, p2_pop

    def repopulate(self, pop, pop_size, pop_id, iteration, ruleset, mutation_rate, verbose):
        """
        Breeds a depleted population until its capacity is reached again.

        Args:
            pop : The population to reproduce from
            pop_size : The capacity of the population
            pop_id : The player ID of the population; 1 or 2
            iteration: The iteration of the players being generated
            ruleset : Ruleset of the game being played
            mutation_rate : Percentage that a mutation will occur
            verbose : Whether to print debug information

        Return:
            A list of children to add to the population
        """
        # Keep track of number of children made
        child_counter = 0

        while len(pop) < pop_size:
            child_counter += 1

            # If the population is too low, repopulate randomly
            if len(pop) < 2:
                if verbose:
                    print("WARNING: Player {} population too low! Repopulating randomly".format(pop_id))
                pop += self.generate_population(pop_size // 2, pop_id)

            # Get two random parents
            parent1, parent2 = sample(pop, 2)

            # Name the child and its strategy
            child_name = "Player {} #{}.{}".format(pop_id, iteration, child_counter)
            child_strat_name = "Evolved Strategy #{}".format(child_counter)

            # Create the child
            child = self.spawn(parent1, parent2, child_name, child_strat_name, mutation_rate)

            # Add the new child to the population
            pop.append(child)

        pop.sort(reverse=True)
