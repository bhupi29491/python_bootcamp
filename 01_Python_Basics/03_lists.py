
# List of integers
my_list = [1, 2, 3]

my_list = ['STRING', 100, 23.2]

print(len(my_list)) # To get the length of the String
print(len(my_list[0])) # To get a specific list item from a list

mylist = ['one', 'two', 'three']

print(mylist[1:]) # O/P : ['two', 'three']  Slicing example

# To concatenate two lists

anotherlist = ['three', 'four', 'five']

print(mylist + anotherlist) # O/P : ['one', 'two', 'three', 'three', 'four', 'five']

# We can mutate a list item
new_list = mylist + anotherlist
print(new_list)   # O/P : ['one', 'two', 'three', 'three', 'four', 'five']

new_list[0] = 'ONE ALL CAPS'
print(new_list)   # O/P : ['ONE ALL CAPS', 'two', 'three', 'three', 'four', 'five']

# To add an element at the end of list
new_list.append('six')
print(new_list) # O/P : ['ONE ALL CAPS', 'two', 'three', 'three', 'four', 'five', 'six']

# To remove an item from end of list
popped_item = new_list.pop()
print('Popped Item : {p}'.format(p=popped_item))  # O/P : Popped Item : six
print(new_list)  # O/P : ['ONE ALL CAPS', 'two', 'three', 'three', 'four', 'five']

# To remove an item from a specific position in a list
print(new_list.pop(0))   # O/P : ONE ALL CAPS
print(new_list)   # O/P : ['two', 'three', 'three', 'four', 'five']

alp_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
print(alp_list.sort())   # O/P : None
print(alp_list)   # OP : ['a', 'b', 'c', 'e', 'x']

sorted_num_list = num_list.sort()
print(type(sorted_num_list))    # O/P : <class 'NoneType'>
sorted_num_list = num_list
print(num_list)             # O/P : [1, 3, 4, 8]

# To reverse list items in a list
num_list.reverse()
print(num_list)   # O/P : [8, 4, 3, 1]

