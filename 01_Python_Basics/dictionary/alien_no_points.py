# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

"""
Output:
Traceback (most recent call last):
File "alien_no_points.py", line 3, in <module>
print(alien_0['points'])
~~~~~~~^^^^^^^^^^
KeyError: 'points'
"""

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)