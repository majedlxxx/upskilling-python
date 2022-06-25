'''
Define multiple majors => computer engineer, .... etc
for each major => name, credit hours, minimum tawjihi grade requirement, list of subjects
student => id, name, major, average
subject => name, credit hours
Instructors => id, name, list of subjects

'''

class Major:
    #name
    #credit hours
    #minimum tawjihi grade requirement
    #list of subjects
    
    def __init__(self, name, credit_hours=132, min_tawjihi_grade = 65, list_of_subject=list()) -> None:
        self.name = name
        self.credit_hours = credit_hours
        self.min_tawjihi_grade = min_tawjihi_grade
        self.list_of_subject = list_of_subject #List of subjects
        
    def __str__(self):
        return self.name

class Student:
    # id, name, major, average
    def __init__(self, id, name, major, average):
        self.id = id
        self.name = name
        self.major = major #Instance of the Major class / not str
        self.average = average
        
    def __str__(self):
        return f'{self.id}:{self.name}'
    

class Subject:
    # name 
    # credit_hours 
    
    def __init__(self, name, credit_hours = 3):
        self.name = name
        self.credit_hours = credit_hours
    
    def __str__(self):
        return self.name

class Instructor:
    #id
    # name
    # list of subjects
    def __init__(self, name, id, list_of_subjects=[]):
        self.name = name
        self.id = id
        self.list_of_subjects = list_of_subjects
    
    def __str__(self):
        return self.name
        



mandatory_subjects = [
    Subject('Calculus 1'),
    Subject('Calculus 2'),
    Subject('Physics 1'),
    Subject('Physics 2'),
    Subject('Databases')
]

optional_subjects = [
    Subject('History'),
    Subject('Soft skills'),
    Subject('Frensh')
]

comminucation_engineering = Major('Communication engineering', 160, 80, mandatory_subjects[:-2])
computer_engineering = Major('Computer engineering', 160, 80, mandatory_subjects)

s1 = Student(1, 'Majed', computer_engineering, 0)
print(s1.id)
print(s1.major)

print(s1.major.list_of_subject)
print(s1.major.list_of_subject[0])
exit()
for x in s1.major.list_of_subject:
    print(x)


