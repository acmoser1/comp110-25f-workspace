"""Define a Pizza class."""


class Pizza:

    # Attributes
    gluten_free: bool
    size: str
    num_toppings: int

    # Constructor
    def __init__(self, gf_input: bool, size_input: str, num_toppings_input: int):
        """Initialize the attribute values."""
        self.gluten_free = gf_input
        self.size = size_input
        self.num_toppings = num_toppings_input

    # Cost Method
    def price(self) -> float:
        """Return the price of a Pizza."""
        cost: float = 0.0
        if self.size == "small":
            cost = 5.25
        else:
            cost = 7.50
        cost += 0.25 * self.num_toppings
        if self.gluten_free is True:
            cost += 1.00
        return cost


# A function that uses an instance (or instances) of a class
def num_orders(pizzas: list[Pizza]) -> int:
    """Tells you how many elements are in pizzas."""
    return len(pizzas)
