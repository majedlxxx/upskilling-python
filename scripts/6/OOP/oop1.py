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
    def __init__(self, xx=3, yy=7): # Constructors are special function always called __init__ will always be called by default when creating objects
        self.x = xx
        self.y = yy
        y = 1 #local variable. will not effect the object
        print("Constructor is called")
        
    def __add__(self, other):
        # self.represent() # This is how you call a method within a function
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        return point(new_x, new_y) #composition => using an instance of the class within the class itself
        
    def represent(self): #self will be discussed later
        print(f"x => {self.x}, y => {self.y}") #if you used x without self.x the interpreter will look for a global variable called x


    def __str__(self):
        return f"x => {self.x}, y => {self.y}"
    
    
    def add_to_x(self, val):
        self.x += val


if __name__ == "__main__":
    p1 = point(1,2)
    print(p1)
    exit()
    p2 = point(3,4)
    point(1 +3 , 2 +4)
    p3 = point(5,10)
    # print(p1 + p2 + 7) #p1 => self, p2 => other
    p1.represent()
    p2.represent()
    p3.represent()

    p4 = p1 + p2
    p4.represent()
    
    p5 = p1 + p2 + p3
    p5.represent()


    exit()
    l = list()
    s = set()
    d = dict()
    test = 0 # object test of type int
    p1 = point() # object p1 of type point
    p1.add_to_x(5)
    print(p1.x)

    p2 = point(20, 10)
    p2.represent()

    print(p1 + p2)
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
