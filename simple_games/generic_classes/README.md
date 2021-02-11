# Generic Classes

Bare-bones classes and interfaces for base-level functionality across games.

### Contents

- Player - Opponents in the game
- Board - Centerpiece of the game
- Game - Logic and structure
- Referee - Legality checks, score keeping, etc.
- Ruleset Interface - Defines the rules of how the game is played
- Strategy Interface - Defines how a player makes a move

### Implementing

The `Player`, `Board`, `Game`, and `Referee` classes should all be imported normally. Both interfaces need to be implemented on newly-created classes that are game-specific. **All functions in the interface must be implemented exactly as they are presented**. Creating a new game is as simple as defining two new classes to implement these interfaces.

When creating a new game, copy and paste the following Markdown to create a `README.md` for that game.
Replace the generic entries with game-specific entries and flesh-out the contents of each section.
Add more if necessary

```
# <Game Name>

A simple two-player game about <brief game summar>.

## Rules

1. Rule 1.
2. Rule 2.
     * Clarifications/notes, if necessary
3. Rule 3.

<more rules, if necessary>

## Visual Example

<Example game play, if possible>.

## Implementation

### The Board

The board's `initial_state` field is <inital state explanation>.

The board's `state` field represents <game state explanation>.

The board's `bounds` is the <bounds/restrictions of the game, if applicable>.

### A Move

A `move` in the game is defined as <what constitutes a move and how it is coded into the ruleset>.

### The Strategies

<Brief notes about strategy implementations>

#### Random

This strategy <explanation of random strategy>.

#### Smart

This strategy should pull data from previous games (within the strategy's `data` field) to determine an optimal move at every possible game state.

### Checking Legality

A move is legal if and only if it matches the following conditions:

1. Condition 1.
2. Condition 2.
<more conditions, if necessary>

### Determining End-Game States

The game has reached an end-game state if and only if the board's `state` is <literal end-game state>.
That is, if and only if <laymans terms of end-game state>.

### Updating the Board

The board's `data` serves as a move history log.
This history is indexed by the current board state, which is <board state data type>.
The values at these indices are tuples in the form `(player name, move made)`.
The board's `state` field is updated by <how board.state is updated>.
```
