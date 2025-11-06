"""File to define Fish class."""

__author__ = "730859653"


class Fish:
    """Defining the Fish class."""

    age: int

    def __init__(self):
        """Constructor for the Fish class."""
        self.age = 0
        return None

    def one_day(self):
        """One day of the fish's life in the river."""
        self.age += 1
        return None
