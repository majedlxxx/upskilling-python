

from ast import expr_context
from textwrap import wrap


def sum_array(arr):
    return sum(arr)




def clean_list(l):
    """
        This function takes a list as an input and return only the float and integers found within that list
    """
    new_list = list()
    for item in l:
        if type(item) not in (int, float):
            continue
        new_list.append(item)
    
    return new_list



def clean_list_decorator(function_name):
    def wrapper():
        # l = [1,2,3, 'test']
        l = function_name()
        new_list = list()
        for item in l:
            if type(item) not in (int, float):
                continue
            new_list.append(item)
        return new_list
            
    return wrapper

@clean_list_decorator
def input_list():
    l = list()
    for i in range(5):
        x = input(">> Enter an element: ")
        try:
            x_int = int(x)
            x = x_int
            
        except:
            try:
                x_float = float(x)
                x = x_float
            except:
                pass
            
        l.append(x)
        
    return l
        
results = input_list()    
print(results)
exit()

arr = ['test', 1, 'test', 2.5, 0]

print(clean_list(arr))
print(sum_array(clean_list(arr)))



def upper_str_decorator(function_name):
    """
        upper case every charecter in any output:
        possible outputs from the below functions => str, list
    """
    def wrapper():
        pass
    return wrapper

@upper_str_decorator
def hello():
    return 'Hello' # => HELLO

@upper_str_decorator
def greeting_message():
    return 'Hello User' # => HELLO USER

@upper_str_decorator
def get_messages():
    return ['test ',  'Hello '] # => ['TEST', 'HELLO ']

