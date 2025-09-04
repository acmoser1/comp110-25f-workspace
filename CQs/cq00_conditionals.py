"""My first COMP110 CQ!"""

__author__ = "730859653"


def guess_a_number() -> None:
    secret: int = 7
    response: int = int(input("Guess a number:"))
    print("Your guess was " + str(response))
    if secret == response:
        print("You got it!")
    elif response < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
