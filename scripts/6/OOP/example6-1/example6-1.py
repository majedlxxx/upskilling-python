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
    def __init__(self, id, name, major, average, optional_subjects=list()):
        self.id = id
        self.name = name
        self.major = major #Instance of the Major class / not str
        self.average = average
        self.optional_subjects = optional_subjects
        
    def get_subjects(self):
        return self.optional_subjects + self.major.list_of_subjects
        
        
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
s2 = Student(2, 'Ahmad', computer_engineering, 0)

# print(s1.id)
# print(s1.major)

# print(s1.major.list_of_subject)



import random
random_subject = random.choice(optional_subjects)
s1.major.list_of_subject.append(random_subject)
s1.optional_subjects.append(random_subject)
# computer_engineering.list_of_subject.append(random_subject)
print(s1.name)
for subject in s1.major.list_of_subject:
    print(subject)
print(s2.name)
for subject in s2.major.list_of_subject:
    print(subject)