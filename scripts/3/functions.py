#Functions

'''
Syntax:
def <function_name>(<parameters>):
    """
    <function_description>
    docstring
    """
    return <value>(Optional)


Calling a function:
function_name(<parameters>)

Parameters:
    1. positional parameters
    2. keyword parameters / named parameters
    3. default parameters
    4. variable number of parameters
    5. variable number of keyword parameters => will be explained later
    6. empty parameters / no parameters

Return value:
    1. I can return a value
    2. I can return nothing
    3. I can return multiple values => not common in other programming languages


After returning from a function by using the return keyword or simply finishing the code execution I will always return to the line after the line in which I called the function.
'''



#positional parameters
def addition(a, b):
    return a + b



print(addition(5, 6))
print(addition(6.5, 1.25))
print(addition("Hello ", "World"))


'''
In the above example, we have used positional parameters.
the first parameter is a and the second parameter is b.
the first value we sent was replaced by 5 and the second value we sent was replaced by 6.
Notice that we can assign a,b to variable of any type, this is possible in python because it's a dynamic language.
'''

print("\n"*5)
#keyword parameters
def division(a, b):
    return a / b

print(division(b=10, a=5))


'''
in the above example, we have used keyword parameters.
to alter the default behavior of the function, where the first parameter is assigned to a and the second parameter is assigned to b, we can use keyword parameters.
'''
print("\n"*5)
#default parameters
def power(a, b=2):
    return a ** b

print(power(2))
print(power(2, 3))

'''
In this case we used default parameters.
if we don't send any value for b, then it will take the default value of 2. else it will take the value we sent.
'''


print("\n"*5)
#Variable number of parameters
def addition(*args): #incomplete function will complete once we explain tuples and loops
    print(args) #args is a tuple => More on that later

print(addition(5, 6, 7,7,8))


'''
In the above example, we have used variable number of parameters.
args is a tuple.
'''

print("\n"*5)
def hello_world(): # return value is None
    print("Hello World")
    
print(hello_world())

def square(length):
    area = length * length
    circumference = length * 4
    return area, circumference # this will return a tuple => more on that later

area, circumference =  square(2)
print(f"Area: {area} Circumference: {circumference}")
