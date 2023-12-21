import math

# Numbers
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
myNumber = pow(100, 2)/100*5+100-499.75
print(myNumber)


# What is the value of the expression 4 * (6 + 5) = 44

# What is the value of the expression 4 * 6 + 5 = 29

# What is the value of the expression 4 + 6 * 5  = 34

# What is the type of the result of the expression 3 + 1.5 + 4? --> float

# What would you use to find a number’s square root, as well as its square?
# For Square we can use pow()
# For Squareroot we can use sqrt()
print(math.sqrt(25))
print(25 ** 0.5)

print(pow(5,2))
print(5 ** 2)

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing
print(s[1])

# Reverse the string 'hello' using slicing:
print(s[::-1])

s ='hello'
# Given the string hello, give two methods of producing the letter 'o' using indexing.

# Method 1:
print(s[4])  # Using forward indexing

# Method 2:
print(s[-1])  # Using backward indexing


# Lists
# Build this list [0,0,0] two separate ways.

# Method 1:
myList = [0, 0, 0]
print(myList)

# Method 2:
list1 = [0] * 3
print(list1)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)
print(sorted(list4))


# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key': 'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Can you sort a dictionary? Why or why not?
# No we cannot sort a dictionary because dictionaries are mappings not a sequence.

# Tuples
# What is the major difference between tuples and lists?
# Tuples are immutable but lists are not.

# How do you create a tuple?
t = (2, 4, 6, 8, 10)
print(t)

# Sets
# What is unique about a set?
# We cannot add duplicate value in set

# Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))


# Booleans
# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

# Operator	Description	Example
# ==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
# !=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
# >	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
# <	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
# >=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
# <=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3  # False
# Answer before running cell
3 <= 2  # False
# Answer before running cell
3 == 2.0    # False
# Answer before running cell
3.0 == 3    # True
# Answer before running cell
4**0.5 != 2  # False
# Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']  # False