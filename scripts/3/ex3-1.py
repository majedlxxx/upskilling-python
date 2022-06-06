'''
While loop practice
1. insert number of students.
2. Enter grade for each student.
3. Print the average grade.
'''

no_of_students = input("Enter number of students: ")
no_of_students = int(no_of_students)

total = 0
student_no = 0

while student_no < no_of_students:
    grade = input("Enter grade: ")
    total += float(grade)
    student_no += 1

print(f"Average grade: {total/no_of_students}")
    
    
'''
Inputs:
number of students
for each student:
        enter student's name
        enter the number of subjects the student has taken
        for each subject:
            enter the subject name
            enter if it's grade is calculated or not
            if it's grade is calculated:
                ask for the grade
        calculate student's average grade
print the student's name with the highest average grade


How will the terminal look like:

Enter number of students: 3

Student 0:
Enter student's name: Ahmad
Enter number of subjects: 2
Enter subject name: Math
should the grade be calculated? (y/n): y
Enter grade: 90
Enter subject name: Social Studies
should the grade be calculated? (y/n): n

Student 1:
.
.


The student with the highest average(90) is Ahmad


'''


