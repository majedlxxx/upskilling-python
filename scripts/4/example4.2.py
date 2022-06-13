students  = list() # list of dictionaries
homeworks = set() # This will be used in case we added homeworks before adding new students
# We chose list to have unique values. and for faster search
#through out this example we are assuming that the student's name is unique.

# empty: [], list()

#pass =>means do nothing

def student_exists(name):  # Replace with find student return index => Later
    for student in students:
        if student['name'] == name:
            return True
    return False # Reaching this line means that I have already looped over the list above and the if statement was never satisfied 
    
'''
[{"name": "Ahmad"}, {"name": "Khalid"}]
student ={"name": "Khalid"}

student_exists("Mahmoud")
'''


def add_student(name, course):
    if student_exists(name):
        print("Student already exists")
        return

    student = {
        "name": name,
        "course": course,
    }

    if len(homeworks) > 0:
        student['homeworks'] = dict()
        for homework in homeworks:
            student['homework'] = 0
    students.append(student)


def change_class(name, course):
    if not student_exists(name): # The condition will only be satisfied if the student doesn't exist
        # the above condition can be replace with: 1. student_exists(name) == False or 2. student_exists(name) != True
        print("User doesn't exist")
        return

    for student in students:
        if student['name'] == name: #=> [{"name": "Ahmad", "course": "Python"}, {"name": "Khalid", "course": "python"}]
            student['course'] = course
            break # or return #No need to continue the loop if I have already found the student
    

def remove_student(name):
    if not student_exists(name):
        print("Student doesn't exist")
        return

    for student in students:
        if student['name'] == name:
            students.remove(student)
            break


def add_homework(homework_name):
    if homework_name in homeworks: # => we used set to have faster search
        print("The Homework exists")
        return
    homeworks.add(homework_name)
    for student in students:
        if 'homeworks' not in student:
            student['homeworks'] = dict() # can be improved
        student["homeworks"][homework_name] = 0
    


def change_grade(name, hw, new_grade):
    if not student_exists(name):
        print("Student doesn't exist")
        return
    
    if hw not in homeworks:
        print("Homework doesn't exist")
        return

    for student in students:
        if student['name'] == name:
            student['homeworks'][hw] = new_grade

def print_report():
    #Printing headers
    print("\n\n********* Student Report *********")
    print("name\t\tcourse", end="")
    for homework in homeworks:
        print(f"\t\t{homework}", end="")
    print() # Just to add a new line
    
    rows = []
    for student in students:
        
        row = f"{student['name']}\t\t{student['course']}"
        for homework in homeworks:
            row += f'\t\t{student["homeworks"][homework]}'
        
        rows.append(row)
    
    for row in rows:
        print(row)
        
    print("*****\n\n")
    
    
    
    # print(students)







#For testing remove it later
def fill_dummy_data():
    add_student("Ahmad", "Python")
    add_student("Khalid", "Python")
    add_homework("Homework 1")
    


fill_dummy_data()

while True:
    print('''Enter:
    1. to add a student
    2. to change student's course
    3. to change student's grade
    4. to add a homework
    5. to grade a homework
    6. to print a report.
    7. remove student
    8. export to excel => Later
    0. to exit
    ''')

    choice = input(">> ").strip()

    if not choice.isnumeric():
        print("Invalid option")
        continue
        
    choice = int(choice) # 1

    if choice not in range(0,8):
        print("Invalid option")
        continue

    if choice == 0:
        break #or use exit()
    
    if choice == 6:
        print_report()

    if choice == 1:
        name = input("Enter student's name: ")
        course = input("Enter course's name: ")
        add_student(name, course)
        
    if choice == 2:
        name = input("Enter student's name: ")
        course = input("Enter course's name: ")
        change_class(name, course)
        #line_after the function call

    if choice == 7:
        name = input("Enter student's name: ")
        remove_student(name)

    if choice == 4:
        homework_name = input("Enter homework's name")
        add_homework(homework_name)
    
    if choice in (3, 5): # or choice == 3 or choice == 5
        name = input("Enter student's name: ")
        # if not student_exists(name): print("Name doesn't exit");continue
        hw = input("Enter homework's name: ")
        new_grade = input("Enter new grade: ")
        change_grade(name, hw, new_grade)

    



print("Exited")

'''
break: breaks us our of a loop => can only be used within a while or a for loops
exit: exits the entire program
use break when you can
'''

'''
Add student
Change class
Change grade
Add Homework
Grade Homework
Print Report

export excel sheet => Later
Link with database => Later
'''





# x = {
#     "name: "Ahmad",
#     "course: "Python",
#     "homeworks":{
#         "Homework 1": 0
#     }
# }