# try except

'''
There is a data type in python Exception that is used to handle errors.
Exception has some subclasses that are used to handle specific errors eg:
1. NameError: NameError is used to handle name errors => eg: print(x), x+=1 etc.
2. ZeroDivisionError: ZeroDivisionError is used to handle division by zero errors => eg: 1/0
3. FileNotFoundError: FileNotFoundError is used to handle file not found errors => eg: open("file.txt", 'r') 
4. TypeError: TypeError is used to handle type errors => a = (1,2); a[0] = 10 / "test" + 1 etc.
5. ValueError: ValueError is used to handle value errors => int("a")
6. FileExistsError: os.mkdir("test") will throw FileExistsError if the directory already exists
7. IndexError: IndexError is used to handle index errors => a = [1,2,3]; a[4]
8. SyntaxError: SyntaxError is used to handle syntax errors => 5/
9. KeyError: KeyError is used to handle key errors => a = {1:2}; a[3]

When you get errors in python usually you get it in the following format:
ExceptionType: ErrorMessage
'''


try:
    print(x) # x is not defined, will cause an error
except:
    print("Something went wrong")

# any error within the try block will be caught by the except block, and will not cause the program to stop


import os

try:
    os.remove('test.txt')
except:
    pass

# Try / Except is used to handle errors but usually it's better to replace it with more logical error handling
if os.path.isfile('test.txt'):
    os.remove('test.txt')
    
    
try:
    print(x)
except FileNotFoundError as error: # except ExceptionType as errorMessage
    print("File not found error ",error)
except NameError as error:
    print("Name error ",error)


# exit()
try:
    open(file_name, 'r')
except NameError as error:
    print("Name error ",error)
    file_name = 'default.txt'
    try:
        open(file_name, 'r')
    except FileNotFoundError as error:
        print("File not found error ",error)

create_folder = input("Do you want to create a folder? (y/n): ")
if create_folder in ('y','Y'):
    folder_name = input("Enter folder name: ")

# 2 possible errors: 
# 1. NameError (folder_name will only be defined if the user answered the previous question with yes) 
# 2. FileExistsError (if the user answered the previous question with yes and the folder already exists) 
try:
    os.mkdir(folder_name)
except NameError as error: # the user answer the previous question with no
    print("Name error ",error)
except FileExistsError as error: # the user answer the previous question with yes and the folder already exists
    print("File exists error ",error)
    
# print(x)


'''
We can always replace any of the exceptionType with the more general Exception class
except Exception as error:
but it's better to use the more specific exceptionType

age = input("Enter your age: ") 

if age.isnumeric(): #prefered solution
    age = int(age) # => I know that this statement might cause an issue, it's better not to execute it until you perform a logical check

Alternatively, we can use the try / except block to handle the error
try:
    age = int(age)
except ValueError as error:
    pass
    
a = [1,2,3]
index = input("Enter index: ")
if index.isnumeric() and int(index) < len(a):
    index = int(index)
    print(a[index])

2 possible solutions:

try:
    index = int(index)
    print(a[index])
except ValueError as error:
    print("Cannot convert to integer")
except IndexError as error:
    print("Index out of range")
    
    
    -----------
    
try:
    index = int(index)
    print(a[index])
except Exception as error:
    print(error)
    

 if I know the this statment will produce an error it's better to not run it unless you perform your checks first



'''

print("Hello")
