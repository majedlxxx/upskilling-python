# Files in python
'''
files openning modes:
    r => read => default mode
    w => write => this will create a new file if it doesn't exist and will erase the content of the file if it exists
    a => append => same as write but it won't erase the content of the file if it exists
    
    Binary modes(Used for binary files like images, pdf): => not covered in this course
    rb => read binary
    wb => write binary
    
    
    w+, r+ => will not be used in this course
    
'''


'''
assume the test-read.txt contains the follwoing:
Hello World
Hi Majed
name
Age
major.
'''


f = open('test-read.txt', 'r') # open the file in read mode / f is a file discriptor

print(f.tell()) # print the current position of the cursor in the file => after openning the file the cursor is at the beginning of the file(0)
data = f.read() # read the entire file(starting from the current cursor postion) / after reading the file the cursor is at the end of the file

print("Data after first read:")
print(data)

print("Data after second read")
print(f.read()) # read the file from the current cursor position to the end of the file => the cursor is at the end of the file so it will return an empty string


f.seek(5) # moves the cursor to the 5th position in the file
print('After using the seek function the cursor position is: ' + str(f.tell()))
print(f.read())

f.seek(0)
print("After resetting the cursor position the cursor position is: " + str(f.tell()))
print(f.read())


print("Reading 2 bytes at a time")
f.seek(0)
print(f.read(2)) # read 2 characters, and move the cursor to the next position

print("Reading until the next new line character")
print(f.readline()) # read the next line character and move the cursor to the next position
print("Reading all lines")
print(f.readlines()) # read all the lines and store them in a list and move the cursor to the next position
f.close() # The code will function normally if we didn't close the file but the file will occupy memory until the program ends


# with keyworkd as a context manager
#Context managers are used to open a file and close it automatically

with open('test-read.txt', 'r') as f: # f = open('test-read.txt', 'r')
    print(f.read())
# file closes automatically when the with statement ends f.close is not needed
print("Done with the file")    


#Don't read large files into memory using the read() function. instead read the file in chunks using readline() or read(int)
# a large file is a file that can occupy a lot of memory

print("Writing to a file")
f = open('test-write.txt', 'w') # open the file in write mode / if the file doesn't exist it will create a new file
# the above statement will empty the file if it exists
# f.read() => won't work because we opened the file in write mode
bytes_written = f.write('Hello World') # write the string to the file and return the number of bytes written
print("Bytes written: " + str(bytes_written))
print("After writing to the file the cursor position is: " + str(f.tell()))
f.seek(5) # moves the cursor to the 5th position in the file
f.write('-') # will erase the space in hello world and replace it with a dash
f.close()

f = open('test-write.txt', 'a') # open the file in append mode
f.write('\ntest')
f.close()
