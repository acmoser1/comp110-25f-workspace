"""File to define Bear class."""

__author__ = "730859653"


class Bear:
    """Defining class Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor for Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day of the Bear's life in the river."""
        self.age += 1  # increase age by 1
        self.hunger_score -= 1  # decrease hunger score by 1 every day
        return None

    def eat(self, num_fish: int):
        """Bear's hunger score increases by num_fish it eats."""
        self.hunger_score += num_fish
        return None
