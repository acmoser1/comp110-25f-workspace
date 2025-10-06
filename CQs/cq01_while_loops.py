"""Practicing using a while loop to iterate over a string."""

__author__ = "730859653"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
        index = index + 1
    return count
