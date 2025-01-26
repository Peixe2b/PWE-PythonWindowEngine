from abc import ABC, abstractmethod # Define interface base class
from typing import Any

class IGame(ABC):
    """Interface for Game"""

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the game"""
        pass

    @abstractmethod
    def update(self, gameTimer: Any) -> None:
        """
        Update the game state based on the game timer.

        Args:
            gameTimer (GameTimer): The game timer object.
        """
        pass

    @abstractmethod
    def draw(self, display: Any) -> None:
        """
        Draw the game state onto the display.

        Args:
            display (Any): The display object.
        """
        pass
