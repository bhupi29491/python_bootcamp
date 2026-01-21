## FileNotFoundError: [Errno 2] No such file or directory: 'demo1.txt'

"""
print('Start line')
fileObject = open('demo1.txt', 'r')
print('Last line')
"""

"""
print('Start line')
fileObject = open('demo.txt', 'r')
print(fileObject)
print("File Name is  :", fileObject.name)
print("File mode is  :", fileObject.mode)
print("is File Object is closed ? :", fileObject.closed)
print('Last line')
"""

### Working with open() & close() methods
"""
print('Start line')
fileObject = open('demo.txt', 'r')
print(fileObject)
print("File Name is  :", fileObject.name)
print("File mode is  :", fileObject.mode)
print("is File Object is closed ? :", fileObject.closed)
fileObject.close()
print("is File Object is closed ? :", fileObject.closed)
print('Last line')
"""

### Working with read() method

"""
fileObject = open("demo.txt", "r")
for i in fileObject:
    print(i, end="\n")
"""

###

"""
fileObject = open("demo.txt", "r")
for i in fileObject:
    print(i, end="")
"""

### Working with read() method

"""
fileObject = open("demo.txt", "r")
data = fileObject.read()  ## reads in the form of multiline string
print(data)
"""

### Find the file length characters

"""
fileObject = open("demo.txt", "r")
data = fileObject.read()  ### reads in the form of multiline string
print(len(data))
"""

### How to find out the total number of words in a given file

"""
fileObject = open("demo.txt", "r")
data = fileObject.read()
print(data.split())
print(len(data.split()), "words available")
"""

### How to find out the total number of lines in a given file

"""
fileObject = open("demo.txt", "r")
data = fileObject.read()
print(data.splitlines())
print(len(data.splitlines()), "lines available")
"""

### Working with read(count) method

"""
fileObject = open("demo.txt", "r")
data = fileObject.read(4)
print(data)

data2 = fileObject.read()
print(data2)
"""

### Working with readline() method

"""
fileObject = open("demo.txt", "r")
data = fileObject.readline()  ## returns in the form of string
print(data)
"""

### Working with readline(count) method

"""
fileObject = open("demo.txt", "r")
data = fileObject.readline(4)
print(data)

data2 = fileObject.readline()
print(data2)
"""

### Working with readlines() method

"""
fileObject = open("demo.txt", "r")
data = fileObject.readlines()  ## returns in the form of list of strings
print(data)
"""

### Working with readlines(count) method

"""
fileObject = open("demo.txt", "r")
data = fileObject.readlines(2)  ## returns in the form of list of single strings
print(data)
"""

### Identify the output

"""
fileObject = open("demo.txt", "r")
data = fileObject.read(4)
print(data)

data2 = fileObject.readlines(2)
print(data2)
"""

### Shortest-way code

"""
print(open("demo.txt", "r").read().split())
print(len(open("demo.txt", "r").read().split()))
"""

### Read last line first word last character and return

"""
print(open("demo.txt", "r").readlines()[-1].split()[0][-1])
"""

### Working with tell() & seek() methods

"""
fileObject = open("demo.txt", "r")
print("Initial File pointer position :", fileObject.tell())  # 0

data = fileObject.read(4)
print(data)
print("After accessing, File pointer position :", fileObject.tell())  # 4

fileObject.seek(0)
print("After using seek() then File pointer position :", fileObject.tell())  # 0
data = fileObject.read(4)
print(data)
"""

### How to find out each word count from a given file & return like a dictionary object

"""
def word_count_from_file(filepath):

    # Reads the file at `filepath`, counts occurrences of each word,
    # and returns a dictionary mapping words to their counts.

    counts = {}  # 1. Initialize empty dictionary

    with open(filepath, 'r', encoding='utf-8') as file:  # 2. Open file safely
        for line in file:  # 3. Iterate through each line
            # 4. Normalize: strip whitespace, lower-case, split on non-word chars
            words = line.strip().lower().split()

            for word in words:  # 5. Iterate words in line
                # 6. Remove punctuation around the word (optional but recommended)
                cleaned = ''.join(char for char in word if char.isalnum())
                if not cleaned:
                    continue  # skip if nothing remains

                # 7. Increment count in dictionary
                if cleaned in counts:
                    counts[cleaned] += 1
                else:
                    counts[cleaned] = 1

    return counts

result = word_count_from_file('demo.txt')
print(result)
"""

