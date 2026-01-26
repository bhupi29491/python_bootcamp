prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input
age = input("How old are you? ")
age = int(age)
print(age>=18)