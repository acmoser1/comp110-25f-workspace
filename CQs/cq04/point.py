from __future__ import annotations

"""Using magic methods to modify the Point class."""

__author__ = "730859653"


class Point:

    # attributes
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Constructor for the Point class."""
        self.x = x
        self.y = y
        # returns self

    # Method __str__
    def __str__(self) -> str:
        """Returns Points in a readable way!"""
        return f"({self.x}, {self.y})"

    # Method __mul__
    def __mul__(self, factor: int) -> Point:
        """Create new point by multiplying old points by factor."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
