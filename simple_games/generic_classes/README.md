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
