"""In this exercise, we will implement a function that contains
Wordle's "game loop"."""

__author__ = "730859653"


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess and continues prompting them
    until they provide a guess of the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def contains_char(word: str, single_character: str) -> bool:
    "Checks if a single character is found in the given word."
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    index: int = 0
    while index < len(word):
        if word[index] == single_character:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compares user's guess to secret word and returns a string of emojis"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    index: int = 0
    emoji_string: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX
        else:
            if contains_char(secret, guess[index]) is True:
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX
        index += 1
    return emoji_string


def main(secret: str = "munch") -> None:
    """The entrypoint of the program and main game loop."""
    expected_length: int = len(secret)
    turn: int = 1
    won: bool = False
    while turn <= 6 and won is False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(expected_length)
        print(emojified(guess, secret))
        if guess == secret:
            won = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if won is False:
        print(f"X/6 - Sorry, try again tomorrow! The word was {secret}")
        return None


if __name__ == "__main__":
    main(secret="munch")
