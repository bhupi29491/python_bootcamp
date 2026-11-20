info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# To get the unique courses
courses_set = set()

for tup in info:
   courses_set.add(tup[1])

print(courses_set)  # {'Science', 'Math', 'English'}

# List students enrolled in English
english_students = []

for name, language in info:
    if language == "English":
        english_students.append(name)
print(english_students)     # ['Alice', 'Charlie']

# Create a dictionary (student, set of courses)
dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)

