def make_pizza(*toppings):  # Using *toppings to accept an arbitrary number of arguments
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza(' mushrooms', 'green peppers', 'extra cheese')

print("===================================================================")


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza(' mushrooms', 'green peppers', 'extra cheese')

print("===================================================================")


# Mixing Positional and Arbitrary Arguments
def make_custom_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_custom_pizza(12, 'pepperoni')
make_custom_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
