"""The goal of this exercise is to decompose programs, solve single problems through
multiple functions, writing and calling functions, and writing a main function."""

__author__: str = "730859653"


def main_planner(guests: int) -> None:
    """Main planner function to coordinate tea party calculations."""
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    total_cost = cost(tea_count, treat_count)
    print(
        f"For {guests} guests, you need {tea_count} tea bags and {treat_count} treats."
    )
    print(f"Total cost: ${total_cost:.2f}")


"""note: interesting how VSCode knows to remember existing code in main_planner def"""


def tea_bags(guests: int) -> int:
    """This function calculates the number of tea bags needed
    for a given number of guests given 2 tea bags per guest."""
    return guests * 2


def treats(guests: int) -> int:
    """This function calculates the number of treats needed for a given
    number of guests, assuming for each tea a guest drinks, they will, on
    average, want 1.5 treats to accompany it.
    """
    return int(tea_bags(guests) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function calculates the total cost given the number of tea bags and treats.
    Assume each tea bag costs $0.50 and each treat costs $0.75."""
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
