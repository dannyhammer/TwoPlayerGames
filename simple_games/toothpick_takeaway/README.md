# Toothpick Takeaway

A simple two-player game about removing toothpicks from a table.

## Rules

1. The game begins with `n` toothpicks on the board.
2. Players take turns removing a number of toothpicks from the pile.
   - Players may only take between 1 and the bounds (default 2) toothpicks.
3. The game ends when no toothpicks are left on the table.

## Visual Example

10 toothpicks remaining, Player 1 draws 2 toothpicks.

8 toothpicks remaining, Player 2 draws 2 toothpicks.

6 toothpicks remaining, Player 1 draws 1 toothpicks.

5 toothpicks remaining, Player 2 draws 2 toothpicks.

4 toothpicks remaining, Player 1 draws 1 toothpicks.

3 toothpicks remaining, Player 2 draws 1 toothpicks.

2 toothpicks remaining, Player 1 draws 2 toothpicks.

0 toothpicks remaining. Player 1 wins.

## Implementation

### The Board

The board's `initial_state` field is the number of toothpicks to place on the table.

The board's `state` field represents how many toothpicks are remaining on the table.

The board's `bounds` is the maximum number of toothpicks a player may take on his/her turn.

### A Move

A `move` in the game is defined as a number representing how many toothpicks the player will take.

### The Strategies

Currently, only a random-choice strategy is defined.

#### Random

This strategy simply chooses a random number of toothpicks between 0 and the board's `bounds`.

#### Smart

This strategy should pull data from previous games (within the strategy's `data` field) to determine an optimal move at every possible game state.

### Checking Legality

A move is legal if and only if it matches the following conditions:

1. The move is a number.
2. The move is greater than 0.
3. The move is less than either the board's `bounds` or the number of toothpicks left on the board, whichever is smaller.

### Examples of Illegal Moves

- 3 toothpicks left, player 2 tries to take 3 toothpicks
- 3 toothpicks left, player 2 tries to take 4 toothpicks
- 3 toothpicks left, player 1 tries to take -1 toothpicks
- player tries to take 0 toothpicks, this violates rule 2

### Determining End-Game States

The game has reached an end-game state if and only if the board's `state` is equal to 0.
That is, if and only if there are no toothpicks left on the table.

### Updating the Board

The board's `data` serves as a move history log.
This history is indexed by the current board state, which is an integer.
The values at these indices are tuples in the form `(player name, move made)`.
The board's `state` field is updated by subtracting the number of toothpicks taken from the board state.
