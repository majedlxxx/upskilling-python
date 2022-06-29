def upper_str_decorator(function_name):
    """
        upper case every charecter in any output:
        possible outputs from the below functions => str, list
    """
    def wrapper():
        output = function_name()
        if type(output) == str:
            return output.upper()
        elif type(output) == list:
            # new_output = list()
            # for item in output:
            #     new_output.append(item.upper())
            # return new_output
            return [item.upper() for item in output]
        else:
            return ""
        
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

# print(upper_str_decorator(hello)) #This will only work if you removed the decorator

print(hello())
print(upper_str_decorator(hello)())# => Will work even if the @ notation is not used with the hello function
print(greeting_message())
print(get_messages())
