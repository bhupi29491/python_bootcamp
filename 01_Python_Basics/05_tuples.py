t = (1, 2, 3)
myList = [1, 2, 3]

# To check the type of the tuples
print(type(t))  # O/P : <class 'tuple'>

# To check the type of the list
print(type(myList))  # O/P : <class 'list'>

# To check the length of the tuples
print(len(t))   # O/P : 3

# Tuples can contain mix object types like string & number
t = ('one', 2)
print(t)    # O/P : ('one', 2)

# To get the first item in the Tuples
print(t[0])     # O/P : one

# To get the last item in the Tuples
print(t[-1])     # O/P : 2

# To get the count of an item exist in the Tuples
t = ('a', 'a', 'b', 'a')
print(t.count('a'))     # O/P : 3

# To get the index of an item exist in the Tuples
t = ('a', 'a', 'b', 'a')
print(t.index('a'))     # O/P : 0
print(t.index('b'))     # O/P : 2

# Tuples are immutable but lists are not
print(myList)   # O/P : [1, 2, 3]
myList[0] = "ONE"
print(myList)   # O/P : ['ONE', 2, 3]

print(t)    # O/P : ('a', 'a', 'b', 'a')
t[0] = "NEW"  # O/P : TypeError: 'tuple' object does not support item assignment








