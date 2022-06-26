class Subject:
    def __init__(self, name: str, credit_hours: int = 3):
        self.name = name
        self.credit_hours = credit_hours
    
    def get_row(self):
        return f"{self.name}, {self.credit_hours}"
    
    def get_columns(self): # replace with __dict__ later
        return 'Subject Name, Credit hours'

    def import_row(self, row_data: str):
        row_data = row_data.strip('\n')
        subject_name, credit_hours = row_data.split(',')
        subject_name = subject_name.strip()
        credit_hours = int(credit_hours.strip()) # might perform integer value check.
        self.name = subject_name
        self.credit_hours = credit_hours
        


    def __str__(self):
        return self.name