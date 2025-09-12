"""Practice with while loops. Will need
an extra variable to track the low card."""


def find_low_card(cards: str) -> int:
    """Loop through a string of numbers and find low number."""
    index: int = 0
    low_card: int = 9
    while index < len(cards):
        if int(cards[index]) < low_card:
            low_card = int(cards[index])
        index = index + 1
    return low_card


print(find_low_card("8675309"))
