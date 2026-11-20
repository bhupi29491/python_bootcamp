alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print("==========================")

# Adding New Key-Value Pairs in Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("==========================")

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print("==========================")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# del alien_0['points']
# print(alien_0)

# Methods in dictionary
print(type(alien_0.keys()))
print(alien_0.keys())   # return all keys
print(alien_0.values())    # return all values
print(alien_0.items())     # return (key, val) pairs
print(alien_0.get('color'))     # return value for that key
alien_0.update({'color': 'red'})
print(alien_0)
