##
# This class is the blueprint for a Genetic Algorithm.
# It contains the functions needed to generate populations, breed players,
# and generate mutations during reproduction.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Penland, Andrew Shelton
#
# Date: 2021-03-20
##

from random import sample, random, randrange
from copy import deepcopy
from . import tournament as t
from . import player as p

class GeneticAlgorithm:

    def __init__(self, ruleset, random_on_init_strat, strat_data, pop_size = 1000, iterations = 100, num_games = 10, fitness = 0.5, max_fitness = 0.9, fitness_increment = 0.025, mutation_rate = 0.025):
        """
        Creates a new Evolution object.

        Args:
            ruleset : The ruleset of the game being evolved upon
            random_on_init_straty: A random-on-initialize strategy constructor used to give each player a random strategy
            strat_data : Data to be fed to the strategy
            pop_size : (Optional) Size of each population to generate
            iterations : (Optional) Number of times to iterate; number of generations to produce
            num_games : (Optional) Minimal number of games each player must compete in during a tournament
            fitness : (Optional) Initial fitness needed for a player to survive
            max_fitness : (Optional) Maximum fitness required for survival
            fitness_increment : (Optional) How much to increment the fitness after each iteration
            mutation_rate : (Optional) Chance that a mutation will occur during reproduction
        """
        self.ruleset = ruleset
        self.random_on_init_strat = random_on_init_strat
        self.strat_data = strat_data
        self.pop_size = pop_size
        self.iterations = iterations
        self.num_games = num_games
        self.fitness = fitness
        self.max_fitness = max_fitness
        self.fitness_increment = fitness_increment
        self.mutation_rate = mutation_rate


    def generate_population(self, pop_size, player_to_gen):
        """
        Generates a population of players with random strategies for the
        Graph Coloring Game.

        Args:
            pop_size : Number of players to generate
            player_to_gen : 1 or 2, depending on what population we are generating

        Return:
            A list of players with random strategies
        """
        # A list to hold the strategies
        strategies = []
        generated = 0
        failures = 0
        max_attempts = 10 * pop_size

        while generated < pop_size:

            # Generate a random strategy 
            strat = self.random_on_init_strat("Basic Data Strategy", self.strat_data)

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

    def spawn(self, parent1, parent2, child_name, child_strat_name):
        """
        Spawns a new `Player` instance using the provided players
        as parents.

        Args:
            parent1 : The first parent
            parent2 : The second parent
            child_name : The name of the child-to-be
            child_strat_name : The name of the child's strategy

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
            if random() < self.mutation_rate:
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

    def evolve(self, verbose = False):
        """
        Generates random populations of players and evolves them across a specified
        number of generations.
        Evolution is composed of competing players, eliminating poor performers,
        and reproducing good players with each other to produce optimal children.

        Args:
            verbose : (Optional) Whether to print debug information

        Return:
            Two lists, containing the elite P1 and P2 populations, respectively
        """
        # Create populations of players with random strategies
        p1_pop = self.generate_population(self.pop_size, 1)
        p2_pop = self.generate_population(self.pop_size, 2)

        for i in range(self.iterations):
            # Create a new tournament for each iteration
            tournament = t.Tournament(self.ruleset, self.num_games, self.fitness)

            # Compete both populations against each other
            p1_pop, p2_pop = tournament.compete(p1_pop, p2_pop)

            if verbose:
                print("\nITERATION: {}, FITNESS: {}".format(i, round(self.fitness, 4)))
                print("\tP1 Pop: " + str(len(p1_pop)))
                print("\tP2 Pop: " + str(len(p2_pop)))

            # Repopulate p1_pop
            self.repopulate(p1_pop, 1, i, verbose)
            self.repopulate(p2_pop, 2, i, verbose)

            # Never increase fitness beyond 90%
            if self.fitness < self.max_fitness:
                self.fitness += self.fitness_increment

        # Return the elite players
        return p1_pop, p2_pop

    def repopulate(self, pop, pop_id, iteration, verbose = False):
        """
        Breeds a depleted population until its capacity is reached again.

        Args:
            pop : The population to reproduce from
            pop_id : The player ID of the population; 1 or 2
            iteration: The iteration of the players being generated
            verbose : (Optional) Whether to print debug information
        """
        # Keep track of number of children made
        child_counter = 0

        while len(pop) < self.pop_size:
            child_counter += 1

            # If the population is too low, repopulate randomly
            if len(pop) < 2:
                if verbose:
                    print("WARNING: Player {} population too low! Repopulating randomly".format(pop_id))
                pop += self.generate_population(self.pop_size // 2, pop_id)

            # Get two random parents
            parent1, parent2 = sample(pop, 2)

            # Name the child and its strategy
            child_name = "Player {} #{}.{}".format(pop_id, iteration, child_counter)
            child_strat_name = "Evolved Strategy #{}".format(child_counter)

            # Create the child
            child = self.spawn(parent1, parent2, child_name, child_strat_name)

            # Add the new child to the population
            pop.append(child)

        pop.sort(reverse=True)
