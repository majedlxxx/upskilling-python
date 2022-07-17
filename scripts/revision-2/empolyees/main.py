"""
    In the below example use FullTimer only
    departments_list = []
    Enter the number of department.
    for each department ask the user for it's name, no_of_employees, then create a department object and add it to the departments_list
    
    employees_list
    Enter the number of employees
    for each employee
        ask for employee's info
        list all departments with their name and indexes in the department_list
        chose the department's index
        create an employee object
        add the employee for the employees list.
    
    create a function call it salary_scale_fix => takes a list of employees as an input. and raise the salaries that are below 500 by 10% \
        and other salaries by 5%
        
    
    Enter the number of departments: 3
    Enter Department name: HR
    Enter Department name: Financial
    Enter Department name: IT
    Enter the number of employees: 5
    Employee 0
    Name: Ahmad
    Birthdate: 5/5/200
    position: Backend Developer
    benefits: Insurance allowance # this should be stored as ["Insurance", "allowance"] use split(" ")
    Chose Department Number:
        0. HR
        1. Financial
        2. IT
    Department No: 0
    Salary: 490
    
    Salaries after fixing the scale:
    Ahmad 539 JODs
    
    

"""
from department import Department

if __name__ == "__main__":
    departments_list = list()
    employees_list = list()
    
    no_of_departments = int(input("Enter the number of apartment: "))
    
    
    for dep in range(no_of_departments):
        print(f"Department {0}:")
        name = input("Name: ")
        no_of_employees = int(input("No of employees: "))
        new_department = Department(name, no_of_employees)
        
        departments_list.append(new_department)
        total_no_of_employees = int(input("Enter the number of employees you want to add: "))
        
        # Loop 1: Ask for employee details name, salary, ...........etc
            # Loop 2: loop over departments and list  their names and indexes
            # assign the department with the chosen index to the employee.
        
        