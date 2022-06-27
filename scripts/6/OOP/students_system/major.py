from subject import Subject
class Major:
    #name
    #credit hours
    #minimum tawjihi grade requirement
    #list of subjects
    
    def __init__(self, name:str, credit_hours = 132, min_tawjihi_grade = 65, list_of_subject = list()):
        self.name = name
        self.credit_hours = credit_hours
        self.min_tawjihi_grade = min_tawjihi_grade
        self.list_of_subject = list_of_subject #List of subjects
        
    def __str__(self):
        return self.name
