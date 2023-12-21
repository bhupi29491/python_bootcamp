# Dictionary example
my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict)  # O/P : {'key1': 'value1', 'key2': 'value2'}

# To get a specific value from dictionary will have to use the key
print(my_dict['key1'])  # O/P : value1

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])  # O/P : 2.99

# Dictionary are super flexible they can hold list or even other dictionary
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}

print(d['k2'])  # O/P : [0, 1, 2]
print(d['k3']['insideKey'])  # O/P : 100

print(d['k2'][2])  # O/P : 2

# To add a new key value pair to an existing dictionary
myDict = {'k1': 100, 'k2': 200}
myDict['k3'] = 300
print(myDict)  # O/P : {'k1': 100, 'k2': 200, 'k3': 300}

# We can override the value of a specific key
myDict['k1'] = 2023
print(myDict)  # {'k1': 2023, 'k2': 200, 'k3': 300}

# Some useful methods of dictionary

# To get all the keys from a dictionary
print(myDict.keys())  # O/P : dict_keys(['k1', 'k2', 'k3'])

# To get all the values from a dictionary
print(myDict.values())  # O/P : dict_values([2023, 200, 300])

# To get all the items from a dictionary
print(myDict.items())  # O/P : dict_items([('k1', 2023), ('k2', 200), ('k3', 300)])

