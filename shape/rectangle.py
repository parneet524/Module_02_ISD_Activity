"""This module defines the Rectangle class."""

__author__ = "Parneet kaur"
__version__ = "1.0.0"

from .shape import Shape

class Rectangle(Shape):
    """Represents a rectangle by its length and width (cm)."""

    def __init__(self, color: str, length: int, width: int) -> None:
        # 1) validate color in superclass
        super().__init__(color)

        # 2) validate numeric types (must be integers per brief)
        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        # 3) protected attributes
        self._length = length
        self._width = width

    def __str__(self) -> str:
        base = super().__str__()  # allowed because Shape.__str__ is not abstract
        return (
            f"{base}\n"
            f"This rectangle has four sides with the lengths of "
            f"{self._length}, {self._width}, {self._length} and {self._width} centimeters."
        )

    def calculate_area(self) -> float:
        # area = length * width
        return float(self._length * self._width)

    def calculate_perimeter(self) -> float:
        # perimeter = length*2 + width*2
        return float(2 * (self._length + self._width))

