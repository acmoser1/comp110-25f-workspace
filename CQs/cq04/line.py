from __future__ import annotations

"""Using magic methods to modify the Line class."""

__author__ = "730859653"
from CQs.cq04.point import Point


class Line:

    # attributes
    p1: Point
    p2: Point

    def __init__(self, p1: Point, p2: Point):
        """Constructor for the Line class."""
        self.p1 = p1
        self.p2 = p2
        # returns self

    # Method __str__
    def __str__(self) -> str:
        """Visualizing Point objects with a line."""
        return f"{self.p1} <-> {self.p2}"

    # Method __mul__
    def __mul__(self, factor: int) -> Line:
        """Creating a new line!"""
        new_p1 = self.p1 * factor
        new_p2 = self.p2 * factor
        new_line: Line = Line(new_p1, new_p2)
        return new_line
