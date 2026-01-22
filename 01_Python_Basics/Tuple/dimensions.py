# If we have a rectangle that should always be a certain size, we can
# ensure that its size doesn’t change by putting the dimensions into a tuple

dimensions = (200, 50)
print(dimensions[0])  # Output: 200
print(dimensions[1])  # Output: 50

# dimensions[0] = 250

"""
Output:
Traceback (most recent call last):
  File "D:\**\Tuple\dimensions.py", line 8, in <module>
    dimensions[0] = 250
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

# Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

print("\n\n------------------------------")


# Writing Over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)