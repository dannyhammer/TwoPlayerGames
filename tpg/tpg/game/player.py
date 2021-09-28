"""
Player

Contains the class definition of a Player in a two-player game.
"""
from .board import Board
from typing import Any
from abc import ABC, abstractmethod

class Player(ABC):
    """
    Represents a single player in a given game.

    Attributes
    ----------
    name : str
        Unique identifier for this player.
    goes_first : bool
        True if this player makes the first move (if this is "Player One").
    data : Any
        Relevant data to influence player strategy.
    wins : int
        Number of games won by this player.
    losses : int
        Number of games lost by this player.
    generation : int
        The generation (or iteration) this player was born during.

    Methods
    -------
    move(self) : Any
        Determines a move for the Player to make in a game.
    """

    def __init__(self, name: str, data: Any = None, generation: int = 0):
        """
        Constructs a new Player instance for a given game.

        Parameters
        ----------
            name : str
                A unique identifier for this player,
            data (optional) : Any
                Relevant data to influence player strategy.
            generation (optional) : int
                The generation (or iteration) this player was born during.
        """
        self.name = name
        self.data = data
        self.generation = generation
        self.goes_first = None
        self.wins = 0
        self.losses = 0

    @abstractmethod
    def move(self, board: Board) -> Any:
        """
        Determines a move for the Player to make in a game.

        May take into account factors such as the Player's strategy, board status, or other influences.

        Parameters
        ----------
            board : Board
                The board whereupon a move is being proposed.

        Returns
        -------
            move : Any
                A move to propose.
        """
        raise NotImplementedError("Must implement abstract method move()")
