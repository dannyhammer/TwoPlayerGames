# Unbalanced Rook

A simple two-player game about moving a Rook across a tileboard.

## Rules

1. The game starts with a tileboard of size `n` x `m`.
2. A Rook is positioned at (0,0), in the top-left of the tileboard.
3. Players alternate moving the Rook any number of spaces either RIGHT or DOWN.
   - Players cannot move two directions in the same turn
   - Players cannot move beyond the bounds of the board.
   - Players must move at least 1 tile per turn.
4. The game ends when either a player submits an invalid move or the player moves the Rook to position (`n`,`m`).

## Visual Example

Denote `R` as the rook and `X` as the end-game destination.

|  R  |     |     |     |     |
| :-: | :-: | --- | :-: | --- |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     | X   |

Consider Player 1 chooses to move RIGHT 3 tiles, the board would be the following:

|     |     |     |  R  |     |
| :-: | :-: | --- | :-: | --- |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     | X   |

Now Player 2 moves DOWN 4 spaces.

|     |     |     |     |     |
| :-: | :-: | --- | :-: | --- |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |  R  | X   |

Player 1 moves a single tile RIGHT.

|     |     |     |     |     |
| :-: | :-: | --- | :-: | --- |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     | R   |

The game has reached an end-game state. Player 1 wins.

## Implementation

### The Board

The board's `state` for Unbalanced Rook is setup as a dictionary in the format `{"D": d, "R": r}`, where `"D"` = DOWN and `"R"` = RIGHT.
`d` and `r` represent how many tiles DOWN and RIGHT, respectively, the Rook has moved.

The board's `initial_state` is set to `{"D": 0, "R": 0}`

The board's `bounds` field is `{"D": n, "R":, m}`, which represents the board's size.

We chose not to use an `(x,y)` coordinate system as this seemed more intuitive. This may be changed later.

### A Move

A `move` in the game is defined as a diction in the format `{"direction": d, "tiles": x}`, where `d` is either `"D"` or `"R"` and `x` is the number of tiles to move in that direction.

### The Strategies

Currently, only a random-movement strategy is defined.

#### Random

This strategy randomly chooses a direction, `D` or `R` initially.
It then calculates the number of tiles between the current Rook position and the board's bounds based on the direction chosen.
Once calculated, it chooses a random number between 1 and the max number of tiles available.
The direction and random number are returned in a dictionary in the `move` format described above.

#### Smart

This strategy should pull data from previous games (within the strategy's `data` field) to determine an optimal move at every possible game state.

### Checking Legality

A move is legal if and only if it matches the following conditions:

1. The move has a `direction` and `tiles` field.
2. The `move["direction"]` field is either `"D"` or `"R"`.
3. The `move["tiles"]` field is greater than `0`.
4. The number of tiles moved will not place the Rook beyond the bounds of the board.

### Example Illegal Moves

- `move[direction] = "T"`
- `move[tiles] = "-1"` or `move[tiles] = "-1200"`

### Determining End-Game States

The game has reached an end-game state if and only if the board's `state` is equal to the board's `bounds`.
That is, if and only if the Rook cannot move any further DOWN or RIGHT.

### Updating the Board

The board's `data` serves as a move history log.
This history is indexed by a `D,R` pair (representing the current position of the Rook).
The values at these indices are tuples in the form `(player name, move made)`.
The board's `state` field is updated by increasing the position of the Rook in the appropriate direction by the number of tiles in the move made.
