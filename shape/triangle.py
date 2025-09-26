"""This module defines the Triangle class."""

__author__ = "Parneet kaur"
__version__ = "1.0.0"

from math import sqrt
from .shape import Shape

class Triangle(Shape):
    """
    A triangle defined by three side lengths (cm).
    """

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """
        Initialize a Triangle with three sides.

        Args:
            color (str): The color of the triangle.
            side_1 (int): Length of side 1 in cm.
            side_2 (int): Length of side 2 in cm.
            side_3 (int): Length of side 3 in cm.

        Raises:
            ValueError: If any side is not an integer.
            ValueError: If the sides do not satisfy the Triangle Inequality Theorem.
        """
        super().__init__(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")

        if not (side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def __str__(self) -> str:
        """
        Return a string description of the triangle.

        Returns:
            str: A formatted string with color and side lengths.
        """
        base = super().__str__()
        return (
            f"{base}\n"
            f"This triangle has three sides with lengths of {self._side_1}, {self._side_2} and {self._side_3} centimeters."
        )

    def calculate_area(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        s = (self._side_1 + self._side_2 + self._side_3) / 2.0
        return float(sqrt(s * (s - self._side_1) * (s - self._side_2) * (s - self._side_3)))

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return float(self._side_1 + self._side_2 + self._side_3)