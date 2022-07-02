class Subject:
    
    def __init__(self, name: str = '-', credit_hours: int = 3):
        self.name = name
        self.credit_hours = credit_hours
    
    def get_row(self):
        return f"{self.name}, {self.credit_hours}"
    
    def get_columns(self): # replace with __dict__ later
        return 'Subject Name, Credit hours'

    def import_row(self, row_data: str): #
        row_data = row_data.strip('\n')
        subject_name, credit_hours = row_data.split(',')
        subject_name = subject_name.strip()
        credit_hours = int(credit_hours.strip()) # might perform integer value check.
        self.name = subject_name
        self.credit_hours = credit_hours
        
    @classmethod #By default cls(class name) is passed as the frist parameter
    def import_from_excel(cls, sheet_name):
        results = list()
        with open(sheet_name, 'r') as f:
            row = f.readline()
            while len(row) > 0:
                row = f.readline()
                if len(row) == 0:
                    break
                subject_name, credit_hours = row.split(',')
                subject_name = subject_name.strip()
                credit_hours = credit_hours.strip('\n').strip(' ')
                credit_hours = int(credit_hours)
                new_subject = cls(subject_name, credit_hours)
                results.append(new_subject)
                
        return results
        
        

    def __str__(self):
        return self.name
    
    
if __name__ == "__main__":
    subjects = Subject.import_from_excel('subjects.csv')
    for s in subjects:
        print(s)