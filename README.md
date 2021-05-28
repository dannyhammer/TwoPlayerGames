# Two-Player Games

Faculty Advisor: Dr. Andrew Penland

Authors: Nicholas O'Kelley, Daniel Hammer, Andrew Shelton

## Introduction

Our current goal is to continue exploring evolutionary game theory on Two Player Games. We are working to make our 
current game code comply with Graph coloring games under the slightly revised rules described in [section two](#Section-Two). 
A more detailed write up of our current progress can be found in the `simple_games` directory in the Jupyter Notebook called `Overview.ipynb`.

## Section One: Generic Two Player Games

The first kind of two-player games we will consider work as follows:

1. There are two players
2. The players alternate turns
3. Both players have the same set of legal moves
4. A player loses if they can not make a move

### Example of a Violation

Chess violates Rule 3: I can not move your pieces, so I don't have the same moves as you.

Two-player graph coloring violates Rule 4. If the second player has no legal moves available, they still win (as long as the graph is not colored).

Nevertheless, this class of games makes a good starting point for our analysis.

## Section Two: Two Player Graph Coloring

Returning to the Graph coloring problem, we began to implement the game following our current game structure and rule definitions. There was one issue: CGC failed to meet all the rules. In our meeting on February 19th 2021, we decided to have our prior rule definitions be the summary of our focus for the Fall semester (2020) and the Spring (2021) focus on a slightly modified rule structure:

1. There are two players
2. The players alternate turns
3. Both players have the same set of legal moves
4. *If either player can't move, player 2 wins.*

This new rule set allows for the Competitive Graph Coloring Game to be added for analysis since there is a win condition for a stalemate.

## Project Structure

- assets
  - images                                                -- The images for the notebooks in this research repository
  - EvolutionaryGameTheoryPoster_MAA-SE_Spring2021.pdf    -- Poster for the MAA SE conference spring 2021
- jupyter_notes                                           -- Holds most of our notes on research and meetings
- simple_games
  - classes                                               -- Holds the generic classes needed for a new game
  - toothpick_takeaway                                    -- Our first game worked on
  - unbalanced_rook                                       -- Our second game worked on
  - Overview.ipynb                                        -- An overview of the project and the current progress being made.

## Current Game Focus

Currently working to produce either a generic csv writer for any game or at minimum one for
each game that way we can collect the data and begin to parse through looking for any patterns that
might be occurring.

## Contribution Standards

In order to have a uniform code commit process, we will follow the idea of
semantic commits.

- The article where we found this is linked [here](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716).
