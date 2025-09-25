"""Creating lists in this exercise."""

__author__ = "730859653"


def all(int_list: list[int], given_int: int) -> bool:
    # base case; check if list's length is 0
    if len(int_list) == 0:
        return False
    # if list exists, run while loop
    index: int = 0
    while index < len(int_list):
        # index cannot be greater than or equal to length of list
        # -> because index of length begins at 0, not 1
        if int_list[index] != given_int:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest integer in a list."""
    # base case; check if list's length is 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    # if list exists, find maximum number in list
    else:
        maximum = input[0]
        index = 1
        # create condition under which to check for max
        while index < len(input):
            number = input[index]
            if number > maximum:
                # if number>max, old max is replaced with number
                maximum = number
            index += 1
        return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    index = 0
    # check if list1 and list2 show deep equality
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True


def extend(list_one: list[int], list_two: list[int]) -> None:
    # add list_one to list_two using += instead of extend
    list_one += list_two
    return None


"""I got confused when implementing this function because I
kept trying to use the append function and was getting an error.
I then tried to use += to see if that would fix the issue, and it did.
I assume using append with 2 lists wouldn't work because you aren't
appending a single integer."""

list_one = [1, 2, 3]
list_two = [7, 8, 9]
