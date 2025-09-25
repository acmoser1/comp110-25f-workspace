"""Practicing List Syntax."""

# Create an empty list of floats called my_numbers
my_numbers: list[float] = list()  # <- constructor
my_numbers: list[float] = []  # <- literal
print(my_numbers)

# Add the value 1.5 to my list
my_numbers.append(1.5)
print(my_numbers)

# Create an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Access element of list using subscription notation
print(game_points[2])

# Modify element of a list
game_points[1] = 72
print(game_points)

"""lists do not support strings!!!"""

# Find the length of a list
print(len(game_points))

# Remove an item from a list
game_points.pop(1)
print(game_points)


def contains(needle: int, haystack: list[int]) -> bool:
    """Check every element in haystack to find if it's equal to needle."""
    index: int = 0
    while index < len(haystack):
        if haystack[index] == needle:
            return True
        index += 1
    # If I've gotten here, I've checked every element and condition was not true
    return False
