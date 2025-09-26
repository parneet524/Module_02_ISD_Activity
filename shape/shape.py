"""This module defines the Shape class."""

__author__ = "Parneet kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for all shapes."""

    def __init__(self, color: str):
        """
        Initialize the shape with a color.
        
        Args:
            color (str): The color of the shape.
        
        Raises:
            ValueError: If color is blank.
        """
        if color is None or color.strip() == "":
            raise ValueError("Color cannot be blank.")
        self._color = color.strip()

    def __str__(self) -> str:
        """
        Return a string representation of the shape.
        
        Returns:
            str: The shape's color.
        """
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Abstract method to calculate the perimeter of the shape."""
        pass
