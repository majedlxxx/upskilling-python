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
# Check lists.py


#Range function

# iteratable objects are objects that can be looped over / iterated over usually can be casted to a list
# range objects are iterable objects that can be looped over / iterated over.
'''
range(start, stop, step)
default value for step is 1
default value for start is 0
end is not included in the range
''' 

arr = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(arr), 2):
    print(arr[i])
    
# For loops
print("\n"*5 + "For loops\n" )
print("With range function")
for i in range(0,4): # range(4) => 0 is the default start value. No need to specify it
    print(i)
    
print("\nWith lists")
for i in [0,1,2,3]:
    print(i)
    
print(list(range(0,4)))

'''
Ex 3.1 rewritten to use for loops
'''
no_of_students = input("Enter number of students: ") #4
no_of_students = int(no_of_students)

total = 0


for i in range(no_of_students):
    grade = input("Enter grade: ")
    total += float(grade)

print(f"Average grade: {total/no_of_students}")



students = ['Ahmad', 'Mohammed', 'Ali', 'Hassan']
# i holds the value of the current element in the list => Ahmad, mohammed, Ali, Hassan
print("\n"*5 + "For loops with lists\n")
for i in students: # Looping over a list 
    print(i)


print("With indexes")
# Lopping over a list using indexes
#i holds the value of the index of the current element in the list => 0, 1, 2, 3

for i in range(len(students)): #for(int i = 0; i < students.length; i++)
    print(students[i])
    


for i, j in zip(range(0,10), range(20,30)): # zip(range(0,10), range(20,30)) => (0,20), (1,21), (2,22), (3,23), (4,24), (5,25), (6,26), (7,27), (8,28), (9,29) Will be discussed later
    print(f"i = {i}, j = {j}")
    
    
for i, j in zip([1,2,3], [4,5,6]):
    print(f"i = {i}, j = {j}")
    
# in the 2 loops below the loop will stop when one of the lists/range is finished.
for i, j in zip(range(20,30), [4,5,6]):
    print(f"i = {i}, j = {j}")
    
for i, j in zip(range(20,23), [4,5,6,7,8]):
    print(f"i = {i}, j = {j}")
    
print(list(enumerate(students))) # => [(0, 'Ahmad'), (1, 'Mohammed'), (2, 'Ali'), (3, 'Hassan')] => index, value
for index, student in enumerate(students):
    print(f"index = {index}, student = {student}")
    
for index in range(len(students)):
    print(f"index = {index}, student = {students[index]}")
    
    
# Filling a list with numbers from 1 to 100

l = []
for i in range(1,101):
    l.append(i)
    
print(l)

# Another way of doing it
l = list(range(1,101))
print(l)

# Method 3:
l = [i for i in range(1,101)]


#Other use cases for loop within a list(One liners)
l = [5**i for i in range(1,11)] # => [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625]


x = '''1
5
7
8
10
48
885'''

l = x.split("\n") #=> ['1', '5', '7', '8', '10', '48', '885']
l = [int(i) for i in l] #=> [1, 5, 7, 8, 10, 48, 885] Now I have a list of integers

