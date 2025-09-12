"""Practicing recursion."""


def f(n: int, b: int) -> int:
    if n == 0:
        return b
    else:
        return f(n - 1, b) + 1
