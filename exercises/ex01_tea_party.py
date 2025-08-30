"""The purpose of this exercise is to plan a tea party and its supplies."""

__author__: str = "730859653"


def main_planner(guests: int) -> None:
    """Plan the tea party by calculating supplies and cost."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


"""note: had challenges understanding why main_planner function had errors,
fixed by letting VSCode add all print statements."""


def tea_bags(guests: int) -> int:
    """
    Calculate the number of tea bags needed for the party assuming each guest
    will use 2 tea bags.
    """
    return guests * 2


"""note: at first, trailhead wouldn't output 2 tea bags per guest, but then
i added guests * 2 in the return statement and it worked."""

"""note: had tourble writing the code because VS code kept filling in code we
haven't learned, messed up autograder."""


def treats(guests: int) -> int:
    """
    Calculate the number of treats needed for the party assuming each guest
    will have 1.5 treats for every tea they drink.
    """
    return int(tea_bags(guests) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculate the total cost of the tea party.
    Assume each tea bag costs $0.50 and each treat costs $0.75.
    """
    return ((tea_count) * 0.5) + ((treat_count) * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
