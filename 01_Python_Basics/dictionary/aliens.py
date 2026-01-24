alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("==============================================")

# automatically generates each alien. In the following example,
# we use to create a fleet of 30 range() aliens

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("....")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

print("==============================================")

# Imagine that one aspect of a game has some aliens
# changing color and moving faster as the game progresses.
# When it’s time to change colors, we can use a for loop and
# an if statement to change the color of the aliens. For
# example, to change the first three aliens to yellow, medium-speed
# aliens worth 10 points each
# turns yellow aliens into red, fast-moving ones worth 15 points each.

# Make an empty list for storing aliens:
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print(".....")