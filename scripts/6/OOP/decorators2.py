

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
        l = function_name()
        new_list = list()
        for item in l:
            if type(item) not in (int, float):
                try:
                    float(item)
                except:
                    continue
            new_list.append(float(item))
        return new_list
            
    return wrapper

@clean_list_decorator
def input_list():
    l = list()
    for i in range(5):
        x = input("Enter an element: ")
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
  

def line_to_list(function_name):
    def wrapper():
        output = function_name()
        return output.split(' ')
    return wrapper

@clean_list_decorator
@line_to_list
def input_list_2():
    data = input(">> ")
    return data

results = input_list_2()
print(results)
  
        
exit()
# results = input_list()    
# print(results)

arr = ['test', 1, 'test', 2.5, 0]

print(clean_list(arr))
print(sum_array(clean_list(arr)))




