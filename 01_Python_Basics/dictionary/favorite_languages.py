# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("=====================================")

# Looping Through All Key-Value Pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("=====================================")

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

print("=====================================")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("=====================================")

if 'erin' not in favorite_languages.keys():
    print("Erin, Please take your poll!")

print("=====================================")

# function to get a sorted() copy of the keys in order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("=====================================")

# method to return a values() sequence of values without any keys.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("=====================================")

# A set is a collection in which each item must be unique
for language in set(favorite_languages.values()):
    print(language.title())

print("=====================================")

# To store each person’s responses in a
# list, people could choose more than one favorite language.

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")

