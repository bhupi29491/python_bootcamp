myFile = open('myfile.txt')

# If wrong file name is passed which is not present then will see the error.
# myFile1 = open('hello.txt')  # O/P : FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'

# To read the content of a file
print(myFile.read())    # O/P : Hello this is a text file.
                              # This is the second line.
                              # This is the third line.

# Since once the file is read. The cursor will move at the end of the file so if we run the read() again
# it will result the output as blank.
print(myFile.read())    # O/P : ''

# To read the file again will have to move the cursor back to the beginning of the file which we can do
# with seek()
myFile.seek(0)
print('--------After seek() method called-----------')
print(myFile.read())

myFile.seek(0)
print(myFile.readlines())   # O/P : ['Hello this is a text file.\n', 'This is the second line.\n',
                                # 'This is the third line.\n']


# Best practices for opening a file. we must ensure once we have read the file then we must close it.
myFile.close()

# Older way to read a file
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)     # O/P : Hello this is a text file.
                              # This is the second line.
                              # This is the third line.


# We can write to a file & can also overwrite the file.
# mode='r' is read only
# mode='w' is write only (will overwrite files or create new!)
# mode='a' is append only (will add on to files)
# mode='r+' is reading & writing
# mode='w+' is writing & reading (Overwrites existing files or creates a new file!)
with open('myfile.txt', mode='r') as newFile:
    contents = newFile.read()
    print(contents)

with open('myfile.txt', mode='a') as f:
    print("--------Append Case------")
    print(f.write('\nThis is the fourth line.'))

with open('myfile.txt', mode='r') as f:
    print(f.read())

with open('hello.txt', mode='w') as f:
    print(f.write("I created this File....!!!"))

with open('hello.txt', mode='r') as f:
    print(f.read())