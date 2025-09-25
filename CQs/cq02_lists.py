"""Mutating functions."""

__author__ = "730859653"


def manual_append(list: list[int], num: int) -> None:
    list.append(num)


my_list = [1, 2, 3]
value_to_add = 4
manual_append(my_list, value_to_add)
print(my_list)


def double(my_list: list[int]) -> None:
    index = 0
    while index < len(my_list):
        my_list[index] = my_list[index] * 2
        index += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
