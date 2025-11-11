from __future__ import annotations


# Write a class called ShoppingGuide
class ShoppingGuide:
    # It should have 3 attributes, groceries: list[str], budget: float, and store: str
    groceries: list[str]
    budget: float
    store: str

    # Write a constructor that takes the parameters:
    # self, groceries: list[str], budget: float, store: str
    # It should update the attribute accordingly
    def __init__(self, groceries: list[str], budget: float, store: str):
        self.groceries = groceries
        self.budget = budget
        self.store = store
        # returns self

    # Write magic method __add__ that takes as parameters self, more_money: float
    # It should return a new ShoppingGuide object with the same attribute values
    # except it should add more_money to the budget
    def __add__(self, more_groceries: list[str]) -> ShoppingGuide:
        """Create a new shopping guide with same attributes, but increased budget."""
        for elem in self.groceries:
            more_groceries.append(elem)
        new_guide: ShoppingGuide = ShoppingGuide(
            more_groceries, self.budget, self.store
        )
        return new_guide

    def __str__(self) -> str:
        info: str = f"At {self.store} with ${self.budget}, buy {self.groceries}"
        return info


# Write a __str__ magic method that gives me all the information of a ShoppingGuide
# object
# Change the __add__ magic method to add a list of more groceries instead of
# adding money to the budget. (Note that it still shouldn’t modify self!)

# Create new variable my_plan that is reference to a ShoppingGuide object
# with the groceries ["apples", "kiwi"], the budget $5.55 and the store "Food Lion".
my_plan: ShoppingGuide = ShoppingGuide(["apples", "kiwi"], 5.55, "Food Lion")
print(my_plan.groceries)
# Now create another variable AJs_plan that is my_plan but with $2.12 added to the
#  budget
AJs_plan: ShoppingGuide = my_plan + ["bread", "eggs"]
print(AJs_plan)
