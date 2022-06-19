import os
from unittest import result





# Collect users input
def get_user_input(no_of_files):
    list_of_files = []

    for i in range(no_of_files):
        file_name = input("Enter file name: ")
        is_file = input("f for file or d for directory: ").strip(" ")
        
        if is_file in ('f','F'):
            is_file = True
        else:
            is_file = False
            
        list_of_files.append((file_name,is_file))
    return list_of_files
    

# Check what's possible and what's not


def check_queries(list_of_files):
    
    results = []
    
    for file in list_of_files:
        error = ""
        check_passed = True
        if os.path.isfile(file[0]) and file[1] == True:
            error = "File exists: " + file[0]
            check_passed = False
        elif os.path.isdir(file[0]) and file[1] == False:
            error = "Directory exists: " + file[0]
            check_passed = False
        elif os.path.exists(file[0]):
            error = "Can't create it because the same file/direcotry with the opposite type exits: " + file[0]
            check_passed = False
        
        results.append({
            'file_name': file[0],
            'is_file': file[1],
            'check_passed': check_passed,
            'error': error
        })
        
    return results


def execute_queries(list_of_files):
    for file in list_of_files:
        if file['check_passed'] == True:
            if file['is_file'] == True:
                open(file['file_name'], 'w').close() # touch file
            else:
                os.mkdir(file['file_name'])
                
        else:
            print(file['error'])
            
            if 'opposite' in file['error']:
                remove = input("Do you want to remove the opposite file/directory? (y/n): ")
                if remove in ('y','Y'):
                    if file['is_file'] == False:
                        os.remove(file['file_name'])
                    else:
                        os.rmdir(file['file_name'])
                    if file['is_file'] == True:
                        open(file['file_name'], 'w').close()
                    else:
                        os.mkdir(file['file_name'])
                
                
if __name__ == "__main__":
    no_of_files = int(input("Enter number of files: "))
    list_of_files = get_user_input(no_of_files)
    list_of_files = check_queries(list_of_files)
    for file in list_of_files:
        print(file)
        
    execute_queries(list_of_files)