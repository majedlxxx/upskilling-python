'''
Enter the number of students:
For each student enter his first name, last name and his age, number of subjects.
of each subject enter the subject name and it's grade.
calculate the average grade of each student.
output

[
{
    "FirstName": "Ahmad",
    "LastName": "Lutfi",
    "Age": 20,
    "grades": {
        "Algebra": 90,
        "English": 80
    }
    "avg": 85.0
},
{
    "FirstName": "...",
    "LastName": "..",
    "Age": 22,
    "grades": {
        "Algebra": 60,
        "Arabic": 80,
        "Calculus": 70
    }
    "avg": 70.0
}


]
'''


n = input("Enter number of students: ")
n = int(n)

results = []

for std in range(n):
    student = dict()
    student["FirstName"] = input("Enter student's first name: ")
    student["LastName"] = input("Enter student's last name: ")
    student["Age"] = int(input("Enter student's age: "))
    student["grades"] = dict()
    no_of_subjects = int(input("Enter number of subjects: "))
    
    
    for sub in range(no_of_subjects):
        sub_name = input("Enter subject name: ")
        student["grades"][sub_name] = float(input("Enter grade: "))
        
    
    total = 0.0
    
    for grade in student["grades"].values():
        total += grade
        
    #The 3 lines above can be replaced with total = sum(student["grades"].values()) => preferred / faster
        
    student["avg"] = total/no_of_subjects
    
    results.append(student)
    
    print("-------------\n\n")
    
    
print(results)