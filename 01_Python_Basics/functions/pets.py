def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Positional Arguments Example
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword Arguments Example
describe_pet(animal_type='cat', pet_name='whiskers')
describe_pet(pet_name='buddy', animal_type='dog')

# Default Values Example
describe_pet('parrot', 'polly')
