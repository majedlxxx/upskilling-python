'''
    
'''

students = {
    'Ahmad':{
        'math': 50,
        'english': 60,
        'programming': 70
    },
    'Khalid':{
        'english': 60,
        'programming': 70
    }
    
}

def get_max_grade(subject_name):
    pass
    

studnets = dict()
no_of_students = int(input("Enter number of students: "))
for std in range(no_of_students):
    name = input("Enter student's name: ")
    subjects_counts = int(input("Enter number of subjects: "))
    grades = dict()
    for sub in range(subjects_counts):
        sub_name = input("Enter subject name: ")
        grades[sub_name] = float(input("Enter grade: "))
    students[name] = grades

print(students)
        
#Collect data.
#Ask for name
#ask for course and it's grade


#Not all the students have all the courses.
#get_max_grade(subject_name) => return highest grade in subject
#get_avg_grade(subject_name) => return average grade in subject

