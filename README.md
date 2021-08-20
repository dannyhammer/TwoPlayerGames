# Two-Player Games

Faculty Advisor: Dr. Andrew Penland

Authors: Nicholas O'Kelley, Daniel Hammer, Andrew Shelton

## Introduction

Our current goal is to continue exploring evolutionary game theory on Two Player Games. We are working to make our 
current game code comply with Graph coloring games under the slightly revised rules described in [section two]("./notes/readme_cont/section2.md"). 
A more detailed write up of our current progress can be found in the `simple_games` directory in the Jupyter Notebook called `Overview.ipynb`.

## Current Scope

Currently in the planning stages for scope of work in the Fall 2021 semester.

## Table of Contents

- [Section One: Generic Games](#-Section-One:-Generic-Two-Player-Games)
    - [Example of Game Violation](#-Example-of-a-Violation)
- [Section Two: Two Player Graph Coloring](#-Section-Two:-Two-Player-Graph-Coloring)
- [Section Three: Creation of New Ideas](#-Creation-of-New-Ideas)
- [Contribution Standards](#-Contribution-Standards)

## Meeting Minutes

Pass meetings notes / minutes can be found [here]("./meeting_minutes/README.md")

## Research Notes

We didn't always keep digital notes, so as they are converted those will be added. New notes are added 
in markdown files or jupyter notebooks [here]("./notes/README.md")

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

------

## Section Two: Two Player Graph Coloring

Returning to the Graph coloring problem, we began to implement the game following our current game structure and rule definitions. There was one issue: CGC failed to meet all the rules. In our meeting on February 19th 2021, we decided to have our prior rule definitions be the summary of our focus for the Fall semester (2020) and the Spring (2021) focus on a slightly modified rule structure:

1. There are two players
2. The players alternate turns
3. Both players have the same set of legal moves
4. *If either player can't move, player 2 wins.*

This new rule set allows for the Competitive Graph Coloring Game to be added for analysis since there is a win condition for a stalemate.

## Section Three: Creation of New Ideas

The big ideas for this section include: 

- What format do we want our research to be written (formal paper, journal, blog post, something for our own sites)?
- Optimizing our repository workflow
- Learning how PyPi works in order to begin to bundle our framework to be pip installable.

## Contribution Standards

- Our Git workflow uses semantic commit messages, more [here](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716).
- Also choose descriptive variable names and document any new functions
