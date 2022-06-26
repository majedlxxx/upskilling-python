class Subject:
    def __init__(self, name: str, credit_hours: int = 3):
        self.name = name
        self.credit_hours = credit_hours
    
    def get_row(self):
        return f"{self.name}, {self.credit_hours}"
    
    def get_columns(self): # replace with __dict__ later
        return 'Subject Name, Credit hours'


    def __str__(self):
        return self.name