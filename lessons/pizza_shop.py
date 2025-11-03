"""Instantiate the Pizza class."""

from lessons.pizza_orders import Pizza, num_orders

addisons_order: Pizza = Pizza(True, "small", 0)
mikaylas_order: Pizza = Pizza(False, "large", 4)
print(addisons_order.price())
print(mikaylas_order.price())

team110_orders: list[Pizza] = [addisons_order, mikaylas_order]

print(num_orders(team110_orders))
