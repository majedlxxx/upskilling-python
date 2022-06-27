# Class level variables
# Instance/object level variable
# Static methods and variables
# Inheritance
class Math: #this class doesn't represent a new data type
    def add(a,b):
        return a + b

    def sub(a,b):
        return a - b
        


class Student:
    id_counter = 0 # Class level attribute # Can be used as a static value.
    def __init__(self, name): #Constructors are optional
        self.id = Student.id_counter
        Student.id_counter += 1
        # x = 'test' # local function variable
        self.name = name # Instance level attribute
        
    def __str__(self):
        return self.name
    
    def describe(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
    

class MastersStudent(Student): #MasterStudent inherits the Student's attribute
    def __init__(self, name, thesis):
        super().__init__(name) #super is a method that returns the superclass / parent class
        # self.name = name
        # self.id = 5
        self.thesis = thesis
        
    def describe(self): # Function overriding
        # print("Name: ", self.name)
        # print("ID: ", self.id)
        super().describe()
        print("Thesis: ", self.thesis)

if __name__ == "__main__":
    
    st = Student('Majed')
    print(isinstance(st, Student)) # => bool: True if t is an instance of the class Test else False

    st.birth_year = 1990 # Instance level attribute
    #Notice that we can add instance level attributes outside the class itself
    print("Student 1:",st.__dict__) #Print all instance level attributes

    st2 = Student('Ahmad')
    st2.avg = 50
    print("Student 2:", st2.__dict__)

    #Student.id += 1 # Modifying instance level attribute
    #print(Student.id)
    
    print(st.id) # First the interpreter will look for an instance attribute if it doesn't exist it will the class level attribute
    
    print(st.id_counter)
    
    print(st.id_counter == st2.id_counter == Student.id_counter)
    #Notice that st and st2 have different instance level attributes despite being objects of the same class
    
    
    
    
    # Inheritance
    print("\n"*3 + "Testing inheritance")
    s1 = Student('Majed')
    s2 = MastersStudent('Ahmad', 'Securing codes')
    
    print(f"Is {s1} a student? ", isinstance(s1, Student))
    print(f"Is {s1} a Masters student? ", isinstance(s1, MastersStudent))
    print(f"Is {s2} a student? ", isinstance(s2, Student))
    print(f"Is {s2} a Masters student? ", isinstance(s2, MastersStudent))


    s1.describe()
    print('----------')
    s2.describe()
