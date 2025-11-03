"""Exercise to implement dictionaries into practice."""

__author__ = "730859653"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary's key-value pairs."""
    inverted: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        # value of inverted dict is the key of input dict
        if value in inverted:  # encounter more than one of same key
            raise KeyError(f"Duplicate key after inversion: {value}")
        inverted[value] = key
        # key of inverted dict is the value of input dict
    return inverted


def favorite_color(favs: dict[str, str]) -> str:
    """Finds favorite color in dictionary."""
    frequency: dict[str, int] = {}
    # count frequency
    for name in favs:
        color = favs[name]
        if color in frequency:
            frequency[color] = frequency[color] + 1
        else:
            frequency[color] = 1
    # find most popular color in dict
    max_count = -1
    # base case, establishes that color must have frequency greater than -1
    most_popular = ""
    for name in favs:
        color = favs[name]
        if frequency[color] > max_count:
            # if current frequency > max, current is new max
            max_count = frequency[color]
            most_popular = color
    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Finds each instance of a color, counts instances."""
    my_dict: dict[str, int] = {}
    for value in values:
        if value in my_dict:
            my_dict[value] = my_dict[value] + 1
            # adds 1 to number of times value appears in dict
        else:
            my_dict[value] = 1
    return my_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Assigns words to their first letter in dictionary."""
    letters_words: dict[str, list[str]] = {}
    for word in words:  # looking through words in the list
        first_letter = word[0]  # stating where first_letter is in word
        if first_letter in letters_words:
            letters_words[first_letter].append(word)
            # add words that begin with letter to list
        else:
            letters_words[first_letter] = [word]
    return letters_words


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates attendance log for a class of students every day."""
    if day in attendance_log:  # checks to make sure day exists in log
        for name in attendance_log[day]:
            if name == student:
                return  # exit loop, don't add duplicate name
        attendance_log[day].append(student)  # add student to existing list
    else:  # if day isn't in log, add student to begin new list
        attendance_log[day] = [student]
    return None
