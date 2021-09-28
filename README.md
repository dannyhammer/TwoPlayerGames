
 ________                            _______  __                                           ______                                          
|        \                          |       \|  \                                         /      \                                         
 \▓▓▓▓▓▓▓▓__   __   __  ______      | ▓▓▓▓▓▓▓\ ▓▓ ______  __    __  ______   ______      |  ▓▓▓▓▓▓\ ______  ______ ____   ______   _______ 
   | ▓▓  |  \ |  \ |  \/      \     | ▓▓__/ ▓▓ ▓▓|      \|  \  |  \/      \ /      \     | ▓▓ __\▓▓|      \|      \    \ /      \ /       \
   | ▓▓  | ▓▓ | ▓▓ | ▓▓  ▓▓▓▓▓▓\    | ▓▓    ▓▓ ▓▓ \▓▓▓▓▓▓\ ▓▓  | ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\    | ▓▓|    \ \▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\  ▓▓▓▓▓▓▓
   | ▓▓  | ▓▓ | ▓▓ | ▓▓ ▓▓  | ▓▓    | ▓▓▓▓▓▓▓| ▓▓/      ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓   \▓▓    | ▓▓ \▓▓▓▓/      ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓    ▓▓\▓▓    \ 
   | ▓▓  | ▓▓_/ ▓▓_/ ▓▓ ▓▓__/ ▓▓    | ▓▓     | ▓▓  ▓▓▓▓▓▓▓ ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓ ▓▓          | ▓▓__| ▓▓  ▓▓▓▓▓▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓▓▓▓▓▓▓_\▓▓▓▓▓▓\
   | ▓▓   \▓▓   ▓▓   ▓▓\▓▓    ▓▓    | ▓▓     | ▓▓\▓▓    ▓▓\▓▓    ▓▓\▓▓     \ ▓▓           \▓▓    ▓▓\▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓\▓▓     \       ▓▓
    \▓▓    \▓▓▓▓▓\▓▓▓▓  \▓▓▓▓▓▓      \▓▓      \▓▓ \▓▓▓▓▓▓▓_\▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓            \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓▓\▓▓▓▓▓▓▓ 
                                                         |  \__| ▓▓                                                                        
                                                          \▓▓    ▓▓                                                                        
                                                           \▓▓▓▓▓▓                                                                         

--- 

Faculty Advisor: Dr. Andrew Penland

Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton

----

## Introduction

Our research focus is on the applications of evolutionary algorithms in game theory as applied
Two Player Games in search of finding optimal winning strategies for each of games. 
Once we have substantial data, we plan to continually analyze the winning trend over the period of games
to see if there are any game agnostic strategies.

A more detailed write up of our current progress can be found in the
`simple_games` directory in the Jupyter Notebook called `Overview.ipynb`. 

### Note: We soon will have a finalized research paper documenting our work 
### through  May 2021.



## Meeting Minutes

Pass meetings notes / minutes can be found in the `meeting_minutes/` directory.
A readme is supplied to organize the different dates.


## Research Notes

We didn't always keep digital notes, so as they are converted those will be
added. New notes are added in markdown files or jupyter notebooks in the
`notes/` directory.

## Section One: Generic Two Player Games

The first kind of two-player games we will consider work as follows:

1. There are two players
2. The players alternate turns
3. Both players have the same set of legal moves
4. A player loses if they can not make a move

### Example of a Violation

Chess violates Rule 3: I can not move your pieces, so I don't have the same
moves as you.

Two-player graph coloring violates Rule 4. If the second player has no legal
moves available, they still win (as long as the graph is not colored).

Nevertheless, this class of games makes a good starting point for our analysis.

------

## Section Two: Two Player Graph Coloring

Returning to the Graph coloring problem, we began to implement the game
following our current game structure and rule definitions. There was one issue:
CGC failed to meet all the rules. In our meeting on February 19th 2021, we
decided to have our prior rule definitions be the summary of our focus for the
Fall semester (2020) and the Spring (2021) focus on a slightly modified rule
structure:

1. There are two players
2. The players alternate turns
3. Both players have the same set of legal moves
4. *If either player can't move, player 2 wins.*

This new rule set allows for the Competitive Graph Coloring Game to be added
for analysis since there is a win condition for a stalemate.

-----

## Section Three: Creation of New Ideas

The big ideas for this section include: 

- What format do we want our research to be written (formal paper, journal,
  blog post, something for our own sites)?
- Optimizing our repository workflow
- Learning how PyPi works in order to begin to bundle our framework to be pip
  installable.

## Contribution Standards

Have a feature that you want to see added? Then fork this repository, craft the
feature, and then open a pull request and we will be in contact with feedback!

Keep in mind: 

- Our Git workflow uses semantic commit messages, more
  [here](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716).
- Descriptive variable names and document any new functions
