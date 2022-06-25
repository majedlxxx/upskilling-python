from subject import Subject
class Instructor:
    #id
    # name
    # list of subjects
    def __init__(self, name: str, id: int, list_of_subjects:list[Subject]=[]):
        self.name = name
        self.id = id
        self.list_of_subjects = list_of_subjects
    
    def __str__(self):
        return self.name
        