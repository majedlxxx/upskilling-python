class Subject:
    def __init__(self, name: str, credit_hours: int = 3):
        self.name = name
        self.credit_hours = credit_hours
    
    def __str__(self):
        return self.name