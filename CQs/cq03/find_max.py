"""function for unit test"""

__author__ = "730859653"


def find_and_remove_max(items: list[int]) -> int:
    max: int = 0
    index = 0
    if items == []:
        return -1
    while index < len(items):
        if items[index] > max:
            max = items[index]
        index += 1
    while index < len(items):
        if items[index] == max:
            items.pop(index)
            index += 1
        else:
            index += 1
    return max
