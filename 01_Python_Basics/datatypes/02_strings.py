print('hello')

print('this is also a string')

print("I'm going on a run")

#  Escape sequence example
print('hello \nworld')  # For new line
print('hello \tworld')  # For tab space

# To check the length of a string. It also counts string.
print(len('hello'))

mystring = "Hello World"
print(mystring[8])

print(mystring[9])   # Through positive indexing
print(mystring[-2])  # Through negative indexing

# Slicing concept
mystring = "abcdefghijk"

# To get the string from index 2 onwards
print(mystring[2:])

# To get the string from start to a specific index. Stop index go up to the index, but it is not include in the output.
print(mystring[:3])

# To get the data between a string
print(mystring[3:6])

# Step size example
print(mystring[::2])

# To reverse a string in Python
print(mystring[::-1])


# String Immutability : It cannot be changed
name = "Sam"
# name[0] = 'P'
last_letters = name[1:]
print('P' + last_letters)

X = 'Hello World'
X = X + " it is beautiful outside!"
print(X)

letter = 'Z'
print(letter * 10)

# Built-in String methods
X = 'Hello World'

print(X.upper()) # upper method to Uppercase a specific string
print(X.lower()) # lower method to Uppercase a specific string
print(X.split()) # split method by default splits the string based on whitespace.

Z = 'Hi this is a string'
print(Z.split('i'))  # We can split based on with some character

# Formatting with .format() method
print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('quick', 'brown', 'fox'))

print('The {0} {0} {0}'.format('quick', 'brown', 'fox'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))  # We can define the variable and use in the main print.

# Float formatting follows "{value:width:precision f}"

result = 100/777
print(result) # O/P : 0.1287001287001287
print("The result was {r:1.3f}".format(r=result)) # O/P : The result was 0.129
print("The result was {r:10.3f}".format(r=result)) # O/P : The result was      0.129


# String literals method : fStrings

name = "Bhupi"
age = 32
print(f'Hello, My name is {name}') # O/P : Hello, My name is Bhupi
print(f'Hello, My name is {name} & I am {age} years old.') # O/P : Hello, My name is Bhupi & I am 32 years old.


