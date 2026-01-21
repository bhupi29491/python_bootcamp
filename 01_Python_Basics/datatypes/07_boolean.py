# In Python, Boolean are the operators that allow you to convey True or False statements.

# Make sure True / False must have first letter as capital Otherwise, Python will coplain.
print(True)    # O/P : True
# print(true)    # O/P : NameError: name 'true' is not defined. Did you mean: 'True'?

print(False)    # O/P : False
# print(false)    # O/P : NameError: name 'false' is not defined. Did you mean: 'False'?

# We can check the type of Boolean
print(type(False))  # O/P : <class 'bool'>

# Comparison operator returns Boolean
print(1 > 2)  # O/P : False
print(1 == 1)  # O/P : True

# We can use None keyword as a placeholder
b = None
print(b)    # O/P : None
print(type(b))  # O/P : <class 'NoneType'>
