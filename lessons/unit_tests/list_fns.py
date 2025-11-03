"""practice with applications of unit tests"""


def get_first(input: list[str]) -> str:
    """return first element of input"""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(inp: list[str]) -> None:
    """remove first element of inp"""
    if len(inp) > 0:  # if not empty
        inp.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """remove and return first element of input"""
    first: str = input[0]
    input.pop(0)
    return first
