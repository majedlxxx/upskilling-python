from hashlib import new
from subject import Subject


def add_student():
    pass

def delete_student():
    pass

def add_major():
    pass

def add_mandatory_subject():
    pass

def add_optional_subject():
    pass

def change_student_major():
    pass


# def get_input_old():
#     number_of_choices = 3
#     print('''
#           1. To add Subject
#           2. To remove Subject
#           0. exit
#           ''')

    
#     while True:
#         try:
#             choice = input('>> ').strip()
#             choice = int(choice)
            
#         except ValueError as e:
#             print("Enter a valid integer")
#             continue
        
        
#         if choice not in range(number_of_choices):
#             print("Enter a valid integer")
#             continue
        
#         break
#     return int(choice)


def export_subjects_to_excel(list_of_subjects):
    rows = list()
    if len(list_of_subjects) == 0:
        return
    rows.append('subject name, credit hours')
    for subject in list_of_subjects:
        rows.append(f'{subject.name}, {subject.credit_hours}')

    with open('subjects.csv', 'w') as f:
        for row in rows:
            f.write(row + '\n')
            
            
def import_subjects_from_excel():
    list_of_subjects = list()
    print("Importing subjects")
    with open('subjects.csv', 'r') as f:
        f.readline()
        for row in f.readlines():
            row_data = row.strip('\n')
            subject_name, credit_hours = row_data.split(',')
            subject_name = subject_name.strip()
            credit_hours = int(credit_hours.strip()) # might perform integer value check.
            new_subject = Subject(subject_name, credit_hours)
            list_of_subjects.append(new_subject)
            # print(row_data)
            
    return list_of_subjects

def export_to_excel(list_of_objects:list, file_name: str):
    if len(list_of_objects) == 0:
        return

    rows = list()
    
    rows.append(list_of_objects[0].get_columns())

    for object in list_of_objects:
        rows.append(object.get_row())
    
    with open(file_name, 'w') as f:
        for row in rows:
            f.write(row + '\n')



def import_from_excel(sheet_name: str,  object_type):
    list_to_fill = list()
    with open(sheet_name, 'r') as f:
        row = f.readline() #column names
        
        while len(row) > 0:

            row = f.readline()
            if len(row) > 0:
                new_object = object_type()
                new_object.import_row(row)
            
                list_to_fill.append(new_object)

    return list_to_fill
            









def get_input():
    number_of_choices = 3
    print('''
          1. To add Subject
          2. To remove Subject
          0. exit
          ''')
    choice = 'a'
    while not choice.isnumeric() or int(choice) not in range(number_of_choices):
        choice = input(">> ")
    
    return int(choice)




if __name__ == "__main__":
    # list_of_subjects = import_subjects_from_excel()
    list_of_subjects = import_from_excel('test.csv', Subject)
    for subject in list_of_subjects:
        print(subject)
    exit()
    print(list_of_subject)
    list_of_majors = list()
    while True:
        choice = get_input()
        if choice == 0:
            export_subjects_to_excel(list_of_subjects)
            export_to_excel(list_of_subjects, 'test.csv')
            exit()
        if choice == 1:
            subject_name = input("Name: ")
            #Error handling for not int values
            credit_hours = int(input("Credit Hours: "))
            
            new_subject = Subject(subject_name, credit_hours)
            
            list_of_subjects.append(new_subject)


            
            
    
    
    

            

