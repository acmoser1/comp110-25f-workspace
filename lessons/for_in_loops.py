"""Practice of for Loops"""

xs: list[str] = ["w", "x", "y", "z"]
index: int = 0
while index < len(xs):
    print(xs[index])
    index += 1

for elem in xs:
    print(elem)


def celebrate(pet_names: list[str]) -> None:
    """Tell every pet they're a good boy!"""
    for pet in pet_names:
        print(f"Good boy{pet}!")


pet_names: list[str] = ["Bear", "Bo", "Louie"]
celebrate(pet_names)

# write a function using range
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")

# "for" loops + dictionaries
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
for key in ice_cream:
    print(key)


def get_orders(orders: dict[str, int]) -> None:
    for flavor in orders:
        print(f"{flavor} has {orders[flavor]} orders.")


get_orders(ice_cream)
