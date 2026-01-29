def greet_users(names):
    """Function to greet each user in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")

usernames = ['alice', 'bob', 'charlie']
greet_users(usernames)