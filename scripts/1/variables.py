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


#substrings / Slicing




