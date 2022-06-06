# Loops

'''
Loops: repeat a block of code a given number of times
2 major types of loops in python:
1. for loop
2. while loop
'''

'''
While loop
Syntax:
while <condition>:
    process
When the condition is true, the loop will continue to run. when the condition is false, the loop will stop. 
'''
i = 0
while i < 5:
    print("test")
    i = i + 1

print("stopped the loop")
print(f"i = {i}")
'''
Tracing the above code
i = 0 is i<5 => true => print("test") / i + 1
i = 1 is i<5 => true => print("test") / i + 1
i = 2 is i<5 => true => print("test") / i + 1
i = 3 is i<5 => true => print("test") / i + 1
i = 4 is i<5 => true => print("test") / i + 1
i = 5 is i<5 => false => stop the loop
'''

# Loop control statements:
'''
1. continue => skip the current iteration and continue with the next iteration
2. break => stop the loop
'''

print("\n"*5)
i=0
while i<10:
    print(i)
    if i == 7:
        break
    i += 1 # => this is the same as i = i + 1, i-=1 is the same as i = i - 1, i*=5 is the same as i = i * 5

print(f"i = {i}")


print("\n"*5)
i = 0
while i<10:
    i += 1
    if i == 7:
        continue
    print(i)
    
# Check example 3.1
