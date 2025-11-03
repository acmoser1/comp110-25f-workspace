"""Exercise with dictionary unit tests."""

__author__ = "730859653"

from exercises.ex04.dictionary import invert
from exercises.ex04.dictionary import favorite_color
from exercises.ex04.dictionary import count
from exercises.ex04.dictionary import alphabetizer
from exercises.ex04.dictionary import update_attendance


# 2 use cases and 1 edge case (KeyError) to test invert function
def test_invert_empty_dict() -> None:
    """Test invert when dict has multiple key-value pair."""
    input_dict: dict[str, str] = {"Addison": "tall", "Lucy": "short"}
    assert invert(input_dict) == {"tall": "Addison", "short": "Lucy"}
    # use case 1


def test_invert_one_pair() -> None:
    """Test invert when dict only has one key_value pair."""
    input_dict: dict[str, str] = {"Addison": "tall"}
    assert invert(input_dict) == {"tall": "Addison"}
    # use case 2


def test_invert_edge_case() -> None:
    """Check that if we call invert on an empty dict, nothing happens."""
    example: dict[str, str] = {}
    invert(example)
    assert example == {}
    # edge case, check that invert doesn't raise issue with empty dict


# 2 use cases and 1 edge case for favorite_color function
def test_favorite_color_popular() -> None:
    """Check that favorite_color returns most popular color."""
    favs: dict[str, str] = {"Addison": "blue", "Lucy": "green", "John": "green"}
    assert favorite_color(favs)
    # use case 1


def test_favorite_color_tie() -> None:
    """Check that favorite_color works when 2 colors are both most popular."""
    input_favs: dict[str, str] = {
        "Addison": "blue",
        "Lucy": "green",
        "John": "green",
        "Steven": "blue",
    }
    assert favorite_color(input_favs) == "blue"
    # use case 2


def test_favorite_color_empty_dict() -> None:
    """Checks behavior of favorite_color when dict is empty."""
    favs: dict[str, str] = {}
    favorite_color(favs)
    assert favs == {}
    # edge case


# 2 use cases and 1 edge case for count function
def test_count_single() -> None:
    """Check if count returns new dictionary if only has 1 color and value."""
    colors: list[str] = ["blue"]
    assert count(colors)
    # use case 1


def test_count_multiple() -> None:
    """Check count when there are multiple colors with varying values."""
    colors: list[str] = ["blue", "blue", "pink", "green", "yellow", "green", "black"]
    assert count(colors)
    # use case 2


def test_count_empty() -> None:
    """Check that count returns nothing if list contains no colors."""
    colors: list[str] = []
    count(colors)
    assert colors == []
    # edge case


# 2 use cases and 1 edge case for alphabetizer function
def test_alphabetizer_existing_letter() -> None:
    """Check that alphabetizer adds word to list with existing letter."""
    words: list[str] = ["perfection", "fun", "party"]
    assert alphabetizer(words)
    # use case 1


def test_alphabetizer_new_letter() -> None:
    """Checks that alphabetizer creates new list when encountering new letter."""
    words: list[str] = ["perfection", "fun", "party", "zebra"]
    assert alphabetizer(words)
    # use case 2


def test_alphabetizer_empty() -> None:
    """Check that aplhabetizer returns no dictionary if list is empty."""
    words: list[str] = []
    alphabetizer(words)
    assert words == []
    # edge case


# 2 use cases and 1 edge case for update_attendance function
def test_update_attendance_add_student() -> None:
    """Check that update_attendance adds student to list if day already exists."""
    log: dict[str, list[str]] = {"Monday": ["Addison"]}
    update_attendance(log, "Monday", "Lucy")
    assert log == {"Monday": ["Addison", "Lucy"]}
    # use case 1


def test_update_attendance_new_day() -> None:
    """Check that update_attendance adds student to list if day doesn't exist."""
    log: dict[str, list[str]] = {"Monday": ["Addison"]}
    update_attendance(log, "Tuesday", "Lucy")
    assert log == {"Monday": ["Addison"], "Tuesday": ["Lucy"]}
    # use case 2


def test_update_attendance_no_duplicate_names() -> None:
    """Checks that update_attendance doesn't add duplicate names on a single day."""
    log: dict[str, list[str]] = {"Monday": ["Addison"]}
    update_attendance(log, "Monday", "Addison")  # duplicate name, don't add to log
    assert log == {"Monday": ["Addison"]}
    # edge case
