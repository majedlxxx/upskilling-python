

'''
You can address any element in the list using indexing => a[0] => gets me the first element in the list. Refer to strings. negative indexing and slicing are also possible.
You can use item assignment to change the value of an element => a[0] = 5
List are flexible => you can add or remove elements from a list => append, insert, pop, remove
append will always add the element to the end of the list
pop will remove the last element in the list and return it
remove will remove the element with the given value
insert will insert the element at the given index
'''


a = [1,3,5,6,2,4,5]

a.append(3) # adds 3 to the end of the list
print(a)
print(f"Number of threes: {a.count(3)}") # returns the number of times 3 appears in the list
print(f"Index of the first three: {a.index(3)}") # returns the index of the first 3 in the list
a.insert(4, 7) # inserts 7 at index 4
print(a)
x = a.pop() # removes the last element in the list and returns it
print("Removed:", x)
print("List:", a)

a.remove(5) # removes the first element with value 5
print("List:", a)

a.reverse() # reverses the list
print("Reversed ",a)
a.sort() # sorts the list ascending
print("Sorted ascendingly: ",a)
a.sort(reverse=True) # sorts the list descending
print("Sorted descendingly: ",a)

b = [-5, -4, -1]
c = a + b
print("After addition")
print("A: ", a)
print("B: ", b)
print("C: ", c)

a.extend(b) # adds the elements of b to the end of a
print("After extending")
print("A: ", a)
print("B: ", b)


print("\n"*5)
a.clear() # removes all elements from the list
a = [1,2,3]
x = 5

x2 = x
a2 = a

print("X", x)
print("X2", x2)
print("A: ",a)
print("A2: ",a2)

print("After appending")
a.append(1)
x += 1
print("X", x)
print("X2", x2)
print("A: ",a)
print("A2: ",a2)

'''
List are different from regular variables in that when you define a variable "a = [1,2,3]" a becomes a pointer pointing at the first element of the list.
a pointer is a variable that contains the address of a list. 
as a value a contains the address of the first element of the list.
if a and b are both lists, a is b will return True if they point to the same list. a == b will return True if they contain the same elements.

in the example above when changing the value of x, x2 won't be affected.
when changing the value of a, a2 will change as well. because a, and a2 are both pointing to the same list.
where
a2 = a will just create another pointer pointing to the same list.
a2 = a.copy() will create a new list and copy the elements of a to it.
'''

print("\n"*5)
a3 = a.copy()
a.append(1)
print("A: ", a)
print("A2: ", a2)
print("A3: ", a3)



#In and not in operators

while True:
    answer = input("Do you have a driving license? (y/n)")
    if answer in ['y', 'n', 'yes', 'no','Y', 'N', 'Yes', 'No']:
        break
    print("Please answer with y or n")



print("Rephrasing:")

while True:
    answer = input("Do you have a driving license? (y/n)")
    if answer not in ['y', 'n', 'yes', 'no','Y', 'N', 'Yes', 'No']:
        print("Please answer with y or n")
    else:
        break


# to create empty lists
x = list()
#or 
x = []

# Lists can contain any type of data including other lists
# Eg:
print("\n"*5)
l = ['Ahmad', 'Majed', 1, 1.2, [1, 5, 3]]
print(l[0])
print(l[3])
print(l[-1])
print(l[-1][1])


# Values unpacking means that you can unpack a multivalue data structure into multiple variables
x, y = [1,2]


'''
 x, y, z = [1,2] => Not enough value to unpack
x, y = [1,2,3] => Too many value to unpack
'''

# str.join(list/tuple/set) => return a string with the elements of the list/tuple/set separated by the string

'--'.join(['a', 'b', 'c']) # returns 'a--b--c'