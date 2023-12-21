mySet = set()
print(mySet)  # O/P : set()

mySet.add(1)
mySet.add(2)
print(mySet)    # O/P : {1, 2}

# We cannot add duplicate value in set
mySet.add(2)
print(mySet)    # O/P : {1, 2}

# sets also does not maintain the order
myList = {1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 4, 4, 4}
print(set(myList))  # O/P : {1, 2, 3, 4, 5}


