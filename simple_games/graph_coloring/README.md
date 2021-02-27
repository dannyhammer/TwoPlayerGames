# Two-Player Graph Coloring

A simple two-player game about coloring a graph.

## Rules

1. The game begins by creating a graph of `n` vertices.
2. Player 1 chooses `k` colors that will be available in the game.
3. Players alternate coloring each vertex of the graph with one of the available `k` colors.
   - A vertex cannot be colored the same color as any of its neighbors.
4. Player 1's goal is to color the entire graph.
5. Player 2's goal is to prevent the entire graph from being colored.
6. The game ends when either the entire graph is colored or there exist a vertex that cannot be colored.

## Visual Example

< TODO: Add visual example of the game (use pictures from old poster?) >

## Implementation

### The Board

The board's `initial_state` field is an uncolored graph, represented by a list of vertices in the following format:

```
initial_state = [
    {"color": 0, "adj": [<adjacent node indices>]},
    {"color": 0, "adj": [<adjacent node indices>]},
    ...
]
```

- The graph is list of dictionaries
- Each dictionary is a vertex, with the index in the list being its ID
- Each vertex has a "color" field, representing what color it is, and an "adj" field, representing its neighbors
- The "adj" field is a list of IDs, with each ID being the ID of a neighboring vertex
- Each vertex's default color is 0

The board's `state` field represents the current graph and its colorings.

The board's `bounds` is the maximum number of colors that can be used in the game.

### A Move

A `move` in the game is defined as a dictionary in the following format:

```
move = {"vertex": <0-n>, "color": <1-k>}
```

Where `vertex` is the vertex to attempt a coloring on and `color` is the color to attempt to use.

### The Strategies

Currently, only random-choice and pseudo-smart strategies are defined.

#### Random

This strategy simply chooses a random vertex and color to attempt as a move.

#### Pseudo-Smart

This strategy chooses the lowest available uncolored vertex and cycles through all of its neighbors to find an available coloring.
If a legal coloring is not available for that vertex, it continues to the next vertex.
If no available legal colorings are available, it returns `None`.

#### Smart

This strategy should pull data from previous games (within the strategy's `data` field) to determine an optimal move at every possible game state.

### Checking Legality

A move is legal if and only if it matches the following conditions:

1. The move is not `None`
2. The vertex chosen is not already colored.
3. No neighbors of the chosen vertex are colored with the same color being attempted.

### Examples of Illegal Moves

- If vertex #1's has a neighbor colors `3` and the attempted coloring for #1 is `3`
- If vertex #2 is already colored and the move attempts to re-color it

### Determining End-Game States

The game has reached an end-game state if one of two conditions is met:

1. All vertices are colored.
2. There exists at least one vertex that cannot be legally colored.

### Updating the Board

The board's `data` serves as a move history log.
This history is indexed by the current board state, which is a stringified representation of the graph.
The values at these indices are tuples in the form `(player name, move made)`.
The board's `state` field is updated by changing the `color` field of the vertex specified in the `move` to the `color` specified in the move.

### Declaring a Winner

A winner is determined based on the current state of the board.
If there are no more uncolored vertices, Player 1 wins.
Otherwise, Player 2 wins.
