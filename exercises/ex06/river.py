"""File to define River class."""

__author__ = "730859653"
from exercises.ex06.fish import Fish
from exercises.ex06.bear import Bear


class River:

    day: int  # tells what day of river's life cycle we are modeling
    fish: list[Fish]  # stores river's fish population
    bears: list[Bear]  # stores river's bear population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_fish = []
        surviving_bears = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish  # Update river's fish pop
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(bears)
        self.bears = surviving_bears  # Update river's bear pop
        return None

    def bears_eating(self):
        for bears in self.bears:
            if len(self.fish) >= 5:  # If there are at least 5 fish in river
                self.remove_fish(3)  # Remove 3 fish from river
                bears.eat(3)  # Bears eat 3 fish removed from river
        return None

    def check_hunger(self):
        """Bears who starve will die."""
        surviving_bears = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                surviving_bears.append(bears)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Modeling reproduction of fish; 2 offspring per fish, 4 per pair."""
        current_fish = len(self.fish)
        new_fish = current_fish * 2
        while current_fish >= 2:
            current_fish += new_fish
        return None

    def repopulate_bears(self):
        """Modeling the reproduction of bears; 1/2 offspring per bear, 1 per pair."""
        current_bears = len(self.bears)
        new_bears = current_bears // 2
        while current_bears >= 2:
            current_bears += new_bears
        return None

    def view_river(self):
        """Prints the status of the river."""
        print(f"~~~Day {self.day}:~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes an amount of fish from River."""
        index = 0
        self.fish.pop(index)
