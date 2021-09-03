"""
Board

Contains the class definition of a game board for a two-player game. Intended to
be inherited from as an abstract class.

A "game board" is an abstract concept. It can be a graph, deck of cards, bag of
marbles, or any other concrete collection of entities on which a game can be
defined and played upon.
"""

from copy import deepcopy
from typing import Any
from abc import ABC, abstractmethod, ABCMeta

class Board(ABC):
    """
    Represents a board in a given game.

    Attributes
    ----------
    initial_state : Any
        The initial state of the game board.
    state : Any
        The current state of the game board.
    history : list
        A history of all moves made on this board

    Methods
    -------
    reset(self) : None
        Resets the board to its original state.
    """

    # Yes, the constructor is marked as an abstract method
    # This prevents people from directly instantiating a Board.
    # Subclassing Board and using super().__init__() will work, though
    @abstractmethod
    def __init__(self, state: Any = None):
        """
        The board constructor initializes the game state and sets game bounds.

        Parameters:
        -----------
            state : Any
                The initial state of the board.
        """
        self.initial_state = deepcopy(state)
        self.state = state
        self.history = list()

    def reset(self) -> None:
        """
        Resets the board to its initial state and erases its history.
        """
        self.state = deepcopy(self.initial_state)
        self.history = list()
