Python library specific organization

Nix: Referee class - have Board/Game check the legality of each move

     Possible: Strategy interface
        - Game specific players instead of player with a toothpick strategy
        - Either in the constructor for a player, could include strategy as a parameter
        - In player parent class the Move() function should have arguments that are appropriate, but should just pass on
        - in child classes, the game specific player will be provided a strategy to use and will have specific move() for the game
        - In larger scale operations, once we know how to represent a strategy in a game then we may find ways to generate them programatically
        - Treat "Player" as an abstract class that contains functions and fields about fitness/comparisons/etc.
        - When making new games, inherit from the Player abstract class and override the abstract "move()" method appropriately for that player
        - Andy takes good notes :D


Change:
Game and Ruleset to become abstract classes - use the above methods and others to create game specific rules and game - most functions will be empty with a simple pass - Ruleset class shall be abstracted into the Game class simliar way to how stratinterface is going into player
