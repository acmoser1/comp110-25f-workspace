"""unit test CQ"""

__author__ = "730859653"

from CQs.cq03.find_max import find_and_remove_max


def test_find_and_remove_max_use_case() -> None:
    """check that find_and_remove_max returns expected value"""
    example: list[int] = [1, 2, 4, 5, 3, 7, 7, 5, 4]
    assert find_and_remove_max(example)


def test_find_and_remove_max_use_case_2() -> None:
    """check that find_and_remove_max mutates input as expected"""
    example: list[int] = [1, 2, 4, 5, 3, 7, 7, 5, 4]
    assert find_and_remove_max(example) == 7
    assert find_and_remove_max(example)


def test_find_and_remove_max_edge_case() -> None:
    """check that find_and_remove_max returns correct value in case
    of an unconventional input"""
    example: list[int] = []
    assert find_and_remove_max(example)
