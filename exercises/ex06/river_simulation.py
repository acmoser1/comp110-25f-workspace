"""Constructing a river with fish and bears."""

__author__ = "730859653"
from exercises.ex06.river import River

my_river: River = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
