from mathops.numops import add, multiply, substract, divide

# import mathops

# When import a file within other folder we use dots
'''
Importing the mathops module from the same directory.
This is a good practice to import modules from the same directory.
This way we can organize our code instead of having all our functions in the same file.
Syntax:
import mathops
from mathops import function_name, function_name2 ...
from mathops import *

'''

print("Select operation:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")


choice = input("Enter choice(1/2/3/4/5):")
choice = int(choice)

if choice == 5:
    exit()

if choice in range(1,5):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
else:
    print("Invalid choice")
    exit()

if choice == 1:
    print(num1,"+",num2,"=",add(num1,num2))

if choice == 2:
    print(num1,"-",num2,"=",substract(num1,num2))
    
if choice == 3:
    print(num1,"*",num2,"=",multiply(num1,num2))

if choice == 4:
    print(num1,"/",num2,"=",divide(num1,num2))
    