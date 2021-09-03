"""
Game

Contains the class definition of a two-player game. Intended to be inherited
from as a parent class.

A "game" is an abstract concept wherein two players compete against each other,
eventually resulting in a winner and a loser (or a stalemate).
"""

from .player import Player
from .board import Board
from typing import Any
from abc import ABC, abstractmethod
from collections.abc import Sequence

class Game(ABC):
    """
    Represents a game to be played by two players.

    Attributes
    ----------
    players : Sequence
        The two players participating in this game.
    current_player : Player
        The player currently making a move in the game; the "attacking" player.
    current_opponent : Player
        The player not making a move; the "defending" player.
    winner : Player
        The winner of this game; declared at the end of play().
    board : Board
        The game board being played on.
    turn : int
        Number of turns elapsed (moves made) in this game.

    Methods
    -------
    is_move_legal(self, player: Player, move: Any) : bool
        Determines if the proposed move is legal in the current game state.
    is_game_over(self) : bool
        Determines if the game is over.
    update_board(self, player: Player, move: Any) : None
        Update the board based on the player's given move.
        Also updates the board's `history` field to log move history.
    declare_winner(self, players) : None
        Declare a winner based on the board's current state and game's rules.
    play(self, verbose: bool = False) : Board
        Executes the given game with the two provided players.
    """

    def __init__(self, players: Sequence[Player, Player], board: Board):
        """
        Constructs a new Game instance to be played on by the provided players.

        Parameters
        ----------
            players : Sequence
                A sequence of the two players competing in this game.
        """
        # Ensure players are of the proper type
        if not issubclass(type(players[0]), Player) or not issubclass(type(players[1]), Player):
            raise TypeError(f"Provided player(s) are not subclasses of {Player}")

        # Ensure two players were provided
        if len(players) != 2:
            raise ValueError(f"Constructor for {__name__} requires two players. Found {len(players)}")

        # Ensure the board is of the proper type
        if not issubclass(type(board), Board):
            raise TypeError(f"Provided board is not subclasses of {Board}")

        self.players = players
        self.current_player = players[0]
        self.current_player.goes_first = True
        self.current_opponent = players[1]
        self.current_opponent.goes_first = False
        self.winner = None
        self.board = board
        self.turn = 0

    @abstractmethod
    def is_move_legal(self, player: Player, move: Any) -> bool:
        """
        Determines if the proposed move is legal in the current game state.

        Parameters
        ----------
            player : Player
                The player proposing the move.
            move : Any
                The move being proposed

        Returns
        -------
            is_legal : bool
                True if the move is legal, else False.
        """
        raise NotImplementedError("Must implement abstract method is_move_legal()")

    @abstractmethod
    def is_game_over(self) -> bool:
        """
        Determines if the game is over.

        Returns
        -------
            is_over: bool
                True if the game is over, else False.
        """
        raise NotImplementedError("Must implement abstract method is_game_over()")

    @abstractmethod
    def update_board(self, player: Player, move: Any) -> None:
        """
        Update the board based on the player's given move.
        Also updates the board's `history` field to log move history.

        Parameters
        ----------
            player : Player
                The player who made the move.
            move : Any
                The move being made.
        """
        raise NotImplementedError("Must implement abstract method update_board()")

    @abstractmethod
    def declare_winner(self) -> None:
        """
        Declare a winner based on the board's current state.
        In many cases, the winner will simply be whoever made the most recent move.
        In these cases, this method does not need to be overriden.
        However, for more complex games, the board's state will need to be considered

        Return:
            winner: Player
                The winning player of the game.
        """
        raise NotImplementedError("Must implement abstract method declare_winner()")


    '''
    def play(self, verbosity: int = 1) -> None:
        """
        Executes the given game with the two provided players.

        Parameters
        ----------
            verbosity (optional) : int
                Specifies how much information should be displayed during a game (higher = more):
                0 - No output.
                1 - Default; Start and end game, players, and winner.
                2 - Board state, current move at each turn.
                3 - Final board state and move history at end of game.
        """
        if verbosity > 0:
            print(f"Starting game: {self.current_player.name} vs {self.current_opponent.name}")

        self.board.reset()

        # Loop until the end-game condition is met
        while not self.is_game_over():
            # Fetch a move from the current player
            move = self.current_player.move(self.board)

            if verbosity > 1:
                print(f"\nBoard: {self.board.state}\nTurn #{self.turn}: {self.current_player.name} -> {move}")

            # If the move is NOT legal, the current opponent wins
            # Regardless of the end-game conditions, "foul behavior" is not permitted
            if not self.is_move_legal(self.current_player, move):
                self.winner = self.current_opponent

                if verbosity > 0:
                    print(f"{self.current_player.name} attempted illegal move.")
                    print(f"Game Over - Winner: {self.winner.name}")

                    if verbosity > 2:
                        print(f"Final State: {self.board.state}")
                        print(f"History: {self.board.history}")

                # No need to continue the loop
                return

            # If the move WAS legal, apply the move to the board
            self.update_board(self.current_player, move)

            # Now increase the turn counter and swap the players
            self.turn += 1
            self.current_player, self.current_opponent = self.current_opponent, self.current_player

        # Game loop has ended; declare winner and return board
        self.winner = self.declare_winner()

        if verbosity > 0:
            print(f"Game Over - Winner: {self.winner.name}")

            if verbosity > 2:
                print(f"Final State: {self.board.state}")
                print(f"History: {self.board.history}")
    '''

    def play(self, verbosity: int = 1) -> None:
        """
        Executes the given game with the two provided players.

        Parameters
        ----------
            verbosity (optional) : int
                Specifies how much information should be displayed during a game (higher = more):
                0 - No output.
                1 - Default; Start and end game, players, and winner.
                2 - Board state, current move at each turn.
                3 - Final board state and move history at end of game.
        """
        if verbosity > 0:
            print(f"Starting game: {self.current_player.name} vs {self.current_opponent.name}")

        self.board.reset()

        # dont worry about this
        self.turn = -1
        self.current_player, self.current_opponent = self.current_opponent, self.current_player

        # Loop until the end-game condition is met
        while not self.is_game_over():
            self.turn += 1
            self.current_player, self.current_opponent = self.current_opponent, self.current_player
            # Fetch a move from the current player
            move = self.current_player.move(self.board)

            if verbosity > 1:
                print(f"\nBoard: {self.board.state}\nTurn #{self.turn}: {self.current_player.name} -> {move}")

            # If the move is NOT legal, the current opponent wins
            # Regardless of the end-game conditions, "foul behavior" is not permitted
            if not self.is_move_legal(self.current_player, move):
                self.winner = self.current_opponent

                if verbosity > 0:
                    print(f"{self.current_player.name} attempted illegal move.")

                # No need to continue the loop
                break

            # If the move WAS legal, apply the move to the board
            self.update_board(self.current_player, move)

        # Game loop has ended; declare winner and return board
        self.winner = self.declare_winner()

        if verbosity > 0:
            print(f"Game Over - Winner: {self.winner.name}")

            if verbosity > 2:
                print(f"Final State: {self.board.state}")
                print(f"History: {self.board.history}")
