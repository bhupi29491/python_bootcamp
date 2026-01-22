# Slicing a List : specify the index of the first and last elements
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])     # Output: ['charles', 'martina', 'michael']

# If you want the second, third, and fourth items in a list
print(players[1:4])     # Output: ['martina', 'michael', 'florence']

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])    # Output: ['charles', 'martina', 'michael', 'florence']

# If you want a slice that includes the end of a list.
print(players[2:])  # Output: ['michael', 'florence', 'eli']

# A negative index returns an element a certain distance from the end of a list
print(players[-3:])  # Output: ['michael', 'florence', 'eli']

# Looping through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

"""
Output:
Here are the first three players on my team:
Charles
Martina
Michael
"""

