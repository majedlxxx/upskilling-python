


T = 10 # Global variable



def f1():
    print(T) #This will work because T is a global variable
    z = 7 # this value can only be used within the function / local variable
    for i in range(5):
        y = 5 #Local variable can only be used within the function
    print(y)


def f2():
    T += 1 # You cannot change the global variable value in a function
    print(T) #This won't work because T now is a local variable and the statement above is not valid
    z = 7 # this value can only be used within the function / local variable
    for i in range(5):
        y = 5 #Local variable can only be used within the function
    print(y)

def f3():
    t = T # A local copy of T is created.
    t += 1 # this will work because t is a local variable
    print(T) #This will work because T is a global variable
    z = 7 # this value can only be used within the function / local variable
    for i in range(5):
        y = 5 #Local variable can only be used within the function
    print(y)

def f4(): # Modifying f2
    global T
    T += 1 # You cannot change the global variable value in a function
    print(T) #This won't work becuase T now is a local variable and the statement above is not valid
    z = 7 # this value can only be used within the function / local variable
    for i in range(5):
        y = 5 #Local variable can only be used within the function
    print(y)


#the below is called the global scope => outside of the function
for i in range(5):
    x = 5 #global variable
    
print(x)

f1()
#f2() #this will not work because T is a global variable and we are trying to change it in a function
print(T)
f3()
f4()
print(T)
# print(z) => z is not defined because z can only be used within the function f1

'''
Global variables are variables that are defined outside of a function.
Global variables are accessible to all functions. => Read only access / you cannot modify it Unless you use the Global keyword.
'''