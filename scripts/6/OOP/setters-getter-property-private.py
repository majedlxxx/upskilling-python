class Test:
    def __init__(self):
        self.__name = "test" # Double underscores at the beginning only used to denote that a variable is private attribute(accessible only within the class)
        # self.age = 22 
    def get_name(self): # Getter
        # self.__name = "test2"
        return self.__name

    @property
    def age(self): # Constant attribute cannot be changed / can't be called as a function
        return 22

    def set_age(self, age):#setter / It won't work because age is a property
        self.age = 22



# t = Test()
# print(t.get_name())
# print(t.__name) # It won't work 

# print(t.age)
# t.set_age(30) #It won't work because age is a property


"""
Property: read access only from main or class.
Private attribute (starting with double underscores): read/write access from the class only 

"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age
    
    @property
    def name(self): # Getter
        return self.__name

    def __test(self) -> None: #methods starting with __ Private method only accessible within the class
        print(self.name, "This is a test")

    def public_test(self) ->  None:
        self.__test()


    def set_name(self, name: str) -> None: # Setter
        self.__name = name


p = Person('Ahmad', 22)
# print(p.__name) This won't work / private attribute
# p.name = "test" This won't work / property
p.x = 5
print(p.x)
p.__name = "test" # here we didn't set the private( attribute __name all it did is defining a new variable __name and giving it the value "test" same as x in the 2 lines above
print(p.__name)
print(p.name) # This will return Ahmad not test
p.set_name('test') # This will change name to test
print(p.name) 
# print(p.__test()) # This won't work / private method
p.public_test()