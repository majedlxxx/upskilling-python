#Lists
l = [1,2,3,4,5]

#Tuples
t = (1,2,3,4,5)


'''
Tuples are immutable.
Tuples don't support item assignment.
We can use indexing to access the items in a tuple, just like we can with a list. But we can't change the items in a tuple.
Tuples have fixed size.
Tuples can hold different types of data.
Tuples are faster than lists.
'''


answer = input("Enter your answer(y/n): ")

if answer in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO'):
    print("Accepted answer")
    

#Sets
a =  {1,2,3,4}    
'''
All values within a set are unique.
To add a value to a list we can use .add method. example below:
a.add(5)
However when try to add a value that already exists in the set, it will not add the value.
Unlike a list where when you add a value to it, it will always be added to the end, where in sets, it will be added in whatever order the interpreter sees fit for faster data retrieval.
sets can hold different types of data.
To create empty set use set() => a = set()

We can use set to get unique values from a list/tuple / remove duplicates from a list/tuple
a = [1,2,34,12,1,1,1,1,1,2,2,2]
a = set(a) => {1, 2, 34, 12}
a = list(a) and back to list
'''

a = {1,2,3}
b = {3,4,5}
c = a.union(b)
print(a) #unchanged
print(b) #unchanged
print(c) #{1,2,3,4,5} will combine all the values in a and b
d = a.intersection(b)
print(a) #unchanged
print(b) #unchanged
print(d) #{3} will only contain the values that are in both a and b

a.add(7)
a.add(7) # Useless / only one 7 will be added
print(a) #{1,2,3,4,7}


a.pop() # Will remove an item from the set(Not first / Not last) => randomly => More on that latter. Not used

a.remove(7) # Will remove the 7 from the set.

a = {1,2,3}
b = {1,2}
print(b.issubset(a)) # Will return True if b is a subset of a. => all elements in b are in a
print(a.issubset(b)) # False because a contains 3 but b doesn't

print(b.issuperset(a)) # Will return True if b is a superset of a. => all elements in a are in b

a.clear() #Clear will empty a set

a = {1,2,3,4}
b = {3,4,5,6}
print(a.difference(b)) # Will return a set of all the elements in a that are not in b we can also use - operator => a - b
a.difference_update(b)  # Will remove all the elements in b from a => a = a - b
print(a)

#Check example 4.1


#Dictionary
'''
To define an empty dictionary use {}, or dict()
a = {} or a = dict()
a = {
    "key1": "value1",
    "key2": "value2",
}
keys can be any type of data.
values can be any type of data.
keys must be unique.
Data is not sorted in a dictionary.
you can use indexing to access the items in a dictionary. => eg: x['LastName']

a["key1"] = "value3" => if key1 does not exist, it will create it. /if key1 exists, it will override the value.

mandatory_subjects = {"algebra": 20, "calculus": 30, "physics": 40}
optional_subjects = {"history": 20, "geography": 30, "literature": 40}
all_subjects = dict()
all_subjects.update(mandatory_subjects) #Will add all the values from mandatory_subjects to all_subjects
all_subjects.update(optional_subjects)
updates = {"algebra": 30, "geography": 40, "Physics": 50} => 2 grades have been modified. we also added physics 
all_subjects.update(updates)

'''
#Check example 4.2, 4.3


# Looping over a dictionary
student = {
    "FirstName": "Ahmad",
    "LastName": "Lutfi",
    "Age": 22,
    "grades": {
        "Algebra": 60,
        "Arabic": 80,
        "Calculus": 70
    },
    "avg": 70.0
}
#Method one

print("\n\n-----------------")
for key in student.keys():
    print(f"{key}: {student[key]}") # print("FirstName: student['FirstName']")

print("\n\nMethod2")
for key in student: #By default will loop over the keys
    print(f"{key}: {student[key]}") 
    
print("\n\nMethod3")
for key, value in student.items(): #=> [('FirstName', 'Ahmad'), ('LastName', 'Lutfi')...]
    print(f"{key}: {value}")


#student.items => zip(student.keys(), student.values())


print("\n\n\n-----------------")
print("FirstName" in student) # Will return True if "FirstName" is in student as a key not a value
print("Ahmad" in student) # Will return False because "Ahmad" is not in student as a key


'''
Next lecture
firstName => xx
grades
    => Algebra: 60

'''

'''
Tuple:
Static data. / Cannot be changed.
allows integer based indexing.a[0]
Used when we have fixed data. 


List
Dynamic data => can be resized, modified ...
allows integer based indexing.a[0]
Used when have dynamic data that can change while running the program.

Set
Dynamic data => can be resized, modified ...
Does not allow any type of indexing => Data is not sorted =>more on that later
Won't allow multiple instances of any value.
We use when want unique data.
Faster data search. => for example when searching for the integer 1 in a set => 1 in a => it's way faster than list or tuples

Dictionary
Dynamic data => can be resized, modified ...
Allows key, value based indexing  => a["firstname"] => "majed"
{
    "firstname": "majed",
    "lastname": "lutfi"
}
We can't repeat a key => this will override the value
'''