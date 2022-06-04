# this is a comment
# Comments are ignored by the interpreter
# Comments are useful for documenting your code
# Comments are useful when you work on a team

'''
    This is a multiline comment
    Docstrings are used to document your code
    Loadded by the interpreter into the mememory.

'''

"""
    This is a multiline comment
    This is a docstring
"""
############## Variables
# Variables are containers for storing data

# examples

#Variable assignment
# variable_name = value
'''
    Value can be called:
    constant
    value
'''

# variable_name = another_variable_name
# variables can be assigned to other variables or constants.
x = 5
y = x
print(x)
print(y)

# variables in python are dynamically typed. that means you can change the type of a variable
'''
    in other programming lanaguges you have to declare the type of the variable.
    eg:
    c/c++:
    int x = 5;
'''

from re import X
from traceback import print_tb


x = 5 # Integer
print(x)
print(type(x))

x = "Hello" # String
print(x)
print(type(x))

x = 1.5 # Float
print(x)
print(type(x))

x = True # Boolean
print(x)
print(type(x))

x = 5.0
print(type(x))

'''
    Data types in python include:
        1. Integer => it is a whole number without decimal point eg: 5, -5, 0
        2. Float => it is a number with decimal point with a fraction eg: 5.5, -5.5, 0.5, 5.0
        3. String => it is a sequence of characters eg: "Hello", "Python", "World"
        4. Boolean => it is a true or false value eg: True, False
    
'''

'''     
    Variables in python are case sensitive.
    Variable names must start with a letter or an underscore.
    variable names cannot start with a number.
    Variables can be reassigned
    
    
    
    eg:
        x => valid
        counter => valid
        x1 => valid
        1x => invalid
        _x => valid
        _1x => valid
        A => valid
        a => valid
        ABC => valid
        abc => valid
        
'''

a = 5
# print(A) => invalid, because variable names are case sensitive
a = 2
A = 3
print(a)
print(A)




'''
    in C/C++ you might use int8_t  to store a number between -127 and 127
    0 to 100
    log(256) = 8 bits can handle numbers from -127 to 127
    int x; => 32 Bits
    int8_t x; => 8 Bits
    
    in python
    x = 5 # the variable will dynamically change it's size
    z = 1212121554454545 # the variable will dynamically change it's size
'''

# operations can be done on variables, or constants:
x = 5 + 7
y = x + 2
print(x)
print(y)




############## Strings
x = "test"
x = 'test'
# In python you can use either single or double quotes to define a string.
x = "he's porgrmming in python"
x = 'he\'s programming in python' # escaping the single quote
x = 'he said "I like python"'
x = "he said \"I like python\""

# escaping a character means using a backslash before the character to escape it's special meaning and take it as is.


# Operations on strings
h = "Hello"
w = "world"
x = h + " " + w
print(X)

# Addition between strings (Concatenation):
x = "Hello " + "World"
print(x)

#multiplaction between strings and integers:
x = "Hello" * 3
print(x)

x = ""



x = "hello this is Majed. I am learning python"
y = x.lower()
print("This is the value of x:")
print(x) # x still has it's original value
print("This is the value of y:")
print(y)# y has the lower case value of x



print(x.lower()) # will lowercase all the cahracters in x
print(x.upper()) # will uppercase all the characters in x
print(x.capitalize()) # will capitalize the first character in x and lowercase the rest

#to check lower's docstring/ documentation
print(x.lower.__doc__)


x = x.lower() 
'''
Since the lower method return a copy of the string, x will not be changed, so to change x we need to
assign the return value of the method to x. //overwrite it's value
'''


x = "    Hello    "
print(x.strip('')) # will remove all the whitespaces from the beginning and the end of the string.
'''
According to strip's docstring: if you don't provide any arguments to strip, it will remove all the whitespaces from the beginning and the end of the string.
else it will remove all the characters in the argument from the beginning and the end of the string.
'''
x = "test"
print(x.strip('t')) # will remove all the 't' characters from the beginning and the end of the string.

x = " test "
print(x.strip('t')) # Nothing will change. because we don't trailing or ending Ts.

print(x.strip(" ").strip("t")) 

print("******* lstrip and rstrip")
x = "test"
print(x.lstrip('t')) # will remove all the 't' characters from the beginning of the string.
print(x.rstrip('t')) # will remove all the 't' characters from the end of the string.

#swapcase
x = "Majed"
print(x.swapcase()) # will swap the case of all the characters in x.

#replace
x = "Hello Ahmad, how are you? ... Ahmad...."
print(x.replace("Ahmad", "Majed")) # will replace all the occurrences of the first argument with the second argument.
print("Original x:")
print(x)
# I can replace to ommit any character in the string for example to ommit spaces:

print(x.replace(' ', ''))


#isnumeric
x = "123"
print(x.isnumeric()) # will return True.
x = "abc"
print(x.isnumeric()) # will return False.
x = "a1"
print(x.isnumeric()) # will return False.
x = "-1234"
print(x.isnumeric()) # will return False.


#startswith
x = "Hello, how are you?"
print(x.startswith('Hello')) # will return True.
print(x.startswith('hello')) # will return False.
print(x.lower().startswith('hello')) # will return True.



#endswith
# is it a question.
print(x.endswith('?')) # will return True.

#split
x = "Hello this is Majed. I live in Amman. I love programming"
print(x.split(".")) # will split the string at the . character and return a list of the substrings. => More on lists later.

#count
print(x.count(' ')) # will return the number of whitespaces in x.

#len of a string
print(len(x)) # will return the length of the string.

# string indexing / substrings / Slicing
x = "Hello"
print(x[0]) # will return the first character of x.
print(x[1]) # will return the second character of x.
# print(x[5]) # Error: IndexError: string index out of range
# Negative indexing:
print(x[-1]) # will return the last character of x.
print(x[-2]) # will return the second last character of x.
# print(x[-6]) # Error: IndexError: string index out of range

'''
In strings you can use the indexing operator to get a substring.
You always start the indexing from 0.
You have to be careful with the indexing not to go out of the string's boundaries.
Indexing range: -len(x) to len(x) - 1 (inclusive)
You can't use assignment to change the value of a character in a string:
x[1] = 'a' # Error: TypeError: 'str' object does not support item assignment
'''


'''
Special characters:
\n => new line
\t => tab
\b => backspace => this won't work if it was followed by a \n
'''

print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\bWorld")

#escape characters
print("Hello\\nWorld")



'''
Slcing is a way to get a substring from a string
Syntax: x[start:end:step] => end is not included
default start is 0
default end is len(x)
default step is 1

x[0:5] will return the substring from the first character to the fifth character.
x[:5] will return the substring from the first character to the fifth character.
x[5:8] will return the substring from the fifth character to the eighth character.
x[7:] will return the substring from the seventh character to the end of the string.
x[0:7:2] will return the substring from the first character to the seventh character with a step of 2. =>x[0], x[2], x[4], x[6]


x[38:34:-1] will return the substring from the 38th character to the 34th character with a step of -1. => it's a good way to reverse a string.
x[::-1] will return the substring from the first character to the last character with a step of -1. => it's a good way to reverse a string.
'''



# print / format / fstring

name = "Majed"
job = "Software Engineer"
age = 26

print("My name is", name, "and I am a", job, "and I am", age, "years old.") # method 1, the arugment sep is being used to separate the arguments with spaces.
print("My name is " + name + " and I am a " + job + " and I am " + str(age) + " years old.") # method 2 concatenation of strings / Casting more on that later
print("My name is {0} and I am a {1} and I am {2} years old.".format(name, job, age)) # method 3 using format
print(f"My name is {name} and I am a {job} and I am {age} years old.") # method 4 using fstring introduced in python 3.6
'''
print arguments:
1) end => it default is \n (new line)
2) sep => it default is " " (space) => what separates the arguments

'''


# Numeric oeprations / boolean operations
'''
Math operations:
 Addition +
 sbutraction -
 multiplication *
 division / => this will always produce a float
 real floor division // => this will always produce an integer => floor(a/b)
 power/Exponents ** 
 modulus %
 
 Priorities:
 1. Parenthesis
 2. Exponents
 3. Modulus
 4. Multiplication and Division(including real floor division)
 5. Addition and Subtraction
 
 
5
 
Bitwise operations:

Or | => if any bit is one the result is one if all bits are zeros the result is zero
and & => if any bit is zero the result is zero if all bits are ones the result is one
xor ^ => if the bits are different the result is one if the bits are the same the result is zero
not ~ => zero becomes one and one becomes zero

priorities:
1. Parenthesis.
2. and &
3. xor ^
4. or |


Logical operations: => used with boolean values
or => if any argument is true the result is true else false
and => if all arguments are true the result is true else false

Priorities:
1. Praenthesis
2. And
3. Or

'''


print("******* Numeric oeprations")
print(f"1+2 = {1+2}")
print(f"1-2 = {1-2}")
print(f"5*2 = {5*2}")
print(f"10/2 = {10/2}")
print(f"5/2 = {5/2}")
print(f"5//2 = {5//2}")
print(f"5%2 = {5%2}")
print(f'5**2 = {5**2}')
print(f'5+2*3 = {5+2*3}')
print(f'5-2/2*11+22 = {5-2/2*11+22}')
print(f'(5-2)/2*11+22 = {(5-2)/2*11+22}')


print("******* Bitwise  oeprations")
print(f"5|2 = {5|2}")
print(f"5&2 = {5&2}")
print(f"5^2 = {5^2}")
print(f"5|2&3 = {5|2&3}")


print("******* Logical oeprations")
print(f"True or False = {True or False}")
print(f"True or True = {True or True}")
print(f"False or False = {False or False}")

print('---------')

print(f"True and False = {True and False}")
print(f"False and False = {False and False}")
print(f"True and True = {True and True}")

'''
True or False and True
True or False
True

'''


# Casting / Type conversion
'''
so far we know the following classes / datatypes:
1. int
2. float
3. str
4. bool
to use casting do the follwing
y = int(x)

int(1.5)
int("1")
int("1.5") # Error: ValueError: invalid literal for int() with base 10: '1.5'
int(False)

float(1)
float("1.5")
float(True)


bool(1)
bool(1.5)
bool(0)

str(1)
str(1.5)
str(True)
'''

#to convert a varaible overwrite it with the new value of the new type
print("Casting example")
x = "5.5"
print(type(x))
x = float(x)
print(type(x))

# User input in python
name  = input("Enter your name: ") # this will take input from the user and store it in the variable name
#name = "Majed"
print(f"Hello {name}")

# the input function will always return a string so you have to use casting to convert it to the type you want
print("Enter your age: ")
age = input("")
print(type(age))
age = int(age)
print(type(age))

# or you can do the follwing age=int(input("Enter your age: "))
















