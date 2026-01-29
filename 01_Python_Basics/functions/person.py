# Returning a Dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {
        'first_name': first_name,
        'last_name': last_name
    }
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)  # Output: {'first_name': 'jimi', 'last_name': 'hendrix'}

musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # Output: {'first_name': 'jimi', 'last_name': 'hendrix', 'age': 27}
