"""Practicing unit tests for my list functions."""

from lessons.unit_tests.list_fns import get_first
from lessons.unit_tests.list_fns import remove_first
from lessons.unit_tests.list_fns import get_and_remove_first

# unit tests to check return value


def test_get_first_use_case() -> None:
    """check that get_first returns first element, "chair"."""
    example: list[str] = ["chair", "desk", "lamp"]
    assert get_first(example) == "chair"


def test_get_first_edge_case() -> None:
    """check that get_first returns empty string when given empty list"""
    example: list[str] = []
    assert get_first(example) == ""


# unit tests to check how the input is modified
def test_remove_first_use_case() -> None:
    """check that remove_first removes the first element"""
    example: list[str] = ["chair", "desk", "lamp"]
    remove_first(example)
    assert example == ["desk", "lamp"]


def test_remove_first_edge_case() -> None:
    """check that if we call remove first on an empty list, nothing happens."""
    example: list[str] = []
    remove_first(example)
    assert example == []


# unit test that checks how input is modified AND return value
def test_get_and_remove_first_use_case() -> None:
    """check that get_and_remove_first both returns and removes first element"""
    example: list[str] = ["chair", "desk", "lamp"]
    assert get_and_remove_first(example) == "chair"
    assert example == ["desk", "lamp"]
