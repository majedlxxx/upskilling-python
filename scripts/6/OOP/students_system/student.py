from major import Major
class Student:
    # id, name, major, average
    def __init__(self, id:int, name:str, major:Major, average:float, optional_subjects:list[Major]=list()):
        self.id = id
        self.name = name
        self.major = major #Instance of the Major class / not str
        self.average = average
        self.optional_subjects = optional_subjects
        
    def get_subjects(self):
        return self.optional_subjects + self.major.list_of_subjects
    
            
        
    def __str__(self):
        return f'{self.id}:{self.name}'