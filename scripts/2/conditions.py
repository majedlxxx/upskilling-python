###### Conditional statements

'''
Syntax:
if <condition>:
    process

---------
if <condition>:
    process1
else:
    process2
    
---------
if <condition>:
    process1
elif <condition2>:
    process2
else:
    process3

'''

# Condition operators:
'''
1. equal to ==, is
2. not equal to !=, is not
3. greater than >
4. less than <
5. greater than or equal to >=
6. less than or equal to <=
used in lists, tuples, dictionaries, sets etc... => more on that later #Review 3/lists.py
8. in
9. not in
10. is
11. is not



'''



print(5>2)
print(3>=5-2)
print(3>5-2)


age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You can Drive")

print("outside the if block")
    
#indentation is important in python because it is a block of code
#indentation error is checked before running the code

#To start a block we use : and indentation(tabs or spaces)
#To end a block we get out of the indentation

'''
you can drive if you are 18 or older
or if you are 16-17 but have your parent's permission
'''

print("-----"+"\n"*3)


#Nested if statements
if age >= 18:
    print("You can drive")
elif age >= 16:
    permission = input("Do you have your parents permission to drive? (y/n): ")
    if permission == 'y':
        print("You can drive")
    else: 
        print("You can't drive")
else: # <16
    print("You can't drive")
    
    
def driver_check(age): # it's bad practice to let the user input anything within the function
    if age >= 18:
        print("You can drive")
    elif age >= 16:
        permission = input("Do you have your parents permission to drive? (y/n): ")
        if permission == 'y':
            print("You can drive")
        else: 
            print("You can't drive")
    else: # <16
        print("You can't drive")
        
driver_check(age)
    
# Practices:
'''
1. Write a program where it takes a green light as an input and then checks if the car is allowed to move or not.
'r' or 'y' => you can't pass
'g' => you can pass

input:
    traffic light
output:
    You can/can't pass
    
2. traffic light + the traffic police man should allow me to pass.
if police man to me to pass I can pass regardless of the traffic light.
if police told me to stop I will have to stop regardless of the traffic light
input:
    police man decision.
    traffic light (might be optional)
output:
    You can/can't pass
'''



'''
in an if statement if you are using the or logical operator
if condition1 or condition2: => true or x is always
    if condition1 is satisfied, condition2 will not be checked

if you are using the and logical operator:
    if condition1 and condition2: => False and x is always False
    if condition1 is not satisfied, condition2 will not be checked
'''





# rewriting driver_check function        
def driver_check(age):
    if age >= 18 or (age >= 16 and input("Do you have your parents permission to drive? (y/n): ") == 'y'):
        print("You can drive")
    else:
        print("You can't drive")
        

print("\n\n\nAfter rewriting the driver_check function")
driver_check(17)

'''
Tracing the flow of driver_check function:
if age >= 18:
    after the first half of the if statement is satisfied the code will print "You can drive"
    the else statement will not be checked
if age < 16:
    the first half of the if statement is not satisfied then the second half of the if statement will be checked and after failing both conditions the else statement will be executed
if age >= 16 and age<18:
    after failing the first half of the if statement the second half of the if statement will be checked => where the user will have to provide his input for parents permission
'''



