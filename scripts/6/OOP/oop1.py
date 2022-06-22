#Refer to theory / oop
# OOP Refers to object oriented programming

#Example
x = 5
print(type(x)) #Note that int is a class and x represents an object/instance of that class
'''
Frequently used datatypes in python
int
float
str

list
tuple
dictionary
set
...

'''

class point:
    #attributes (x,y)
    x = 3
    y = 7
    
    
    #Self: is an instance of the class "point" we use it to access attributes and functions within the class
    #Methods: functions within classes are called method
    
    #For each method within the class let the first argument always be self
    def __init__(self, x=3, y=7): # Constructors are special function always called __init__ will always be called by default when creating objects
        self.x = x
        self.y = y
        print("Constructor is called")
        
    def represent(self): #self will be discussed later
        print(f"x => {self.x}, y => {self.y}") #if you used x without self.x the interpreter will look for a global variable called x


    def add_to_x(self, val):
        self.x += val



l = list()
s = set()
d = dict()
test = 0 # object test of type int
p1 = point() # object p1 of type point
p1.add_to_x(5)
print(p1.x)

p2 = point(20, 10)
p2.represent()
exit()


p1.__init__()


print(p1.x)
print(p1.y)
p1.represent()

print(point)
print(p1)

p1 = point() # 2, 7
p2 = point() # 3, 7
p3 = p1 # 3, 7
p1.x = 2
print("p1: ")
p1.represent()
print("p2: ")
p2.represent()
print("p3: ")
p3.represent()
print(p1)
print(p2)
print(p3)
#For each object of type point we create a copy of x, and y will be created. Notice in the example above when I changed p1.x, p2.x remained untouched
#Notice that changing p1 will also change p3 since p1, and p3 are just pointers pointing to the same memory location
