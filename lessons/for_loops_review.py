"""practice with for loops after the quiz"""


def for_loop(items: list[str]) -> str:
    """print every element in items and return last element"""
    for x in items:
        print(x)
    return x


animals: list[str] = ["monkey", "zebra", "snake"]
for_loop(animals)


def for_range_loop(items: list[str]) -> str:
    """print every element in items ans return the last element"""
    for idx in range(0, len(items)):
        print(idx)
    return items[idx]
