from subject import Subject


class Employee:
    id_counter = 0
    def __init__(self, name = "", salary = 0, starting_date = '1/1/2020', vacation_days = 14, sick_leaves = 14):
        self.name = name
        self.salary = salary
        self.starting_date = starting_date
        self.vacation_days = vacation_days
        self.sick_leaves = sick_leaves
        self.id = Employee.id_counter
        Employee.id_counter += 1
        
    def describe(self):
        print("name: ", self.name)
        print("salary: ", self.salary)
        print("starting_date: ", self.starting_date)
        print("vacation_days: ", self.vacation_days)
        print("sick_leaves: ", self.sick_leaves)
        print("id: ", self.id)


        
        
        
        
    
        

class Instructor(Employee):

    def __init__(self, name = "", salary = 0, starting_date = '1/1/2020', vacation_days = 14, sick_leaves = 14, list_of_subjects = list()):
        super().__init__(name, salary, starting_date, vacation_days, sick_leaves)
        self.list_of_subjects = list_of_subjects
    
    def describe(self):
        super().describe()
        print("Subjects: ", self.list_of_subjects)
        

    def __str__(self):
        return self.name
        