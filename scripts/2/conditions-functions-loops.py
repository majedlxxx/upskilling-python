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
used in lists, tuples, dictionaries, sets etc... => more on that later
8. in
9. not in



'''

from certifi import where


print(5>2)
print(3>=5-2)
print(3>5-2)


age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You can Drive")

print("outside the if block")
    
#identation is important in python because it is a block of code
#identation error is checked before running the code

 
'''
you can drive if you are 18 or older
or if you are 16-17 but have your parent's permission
'''

print("-----"+"\n"*3)

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
    
    
def driver_check(age):
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