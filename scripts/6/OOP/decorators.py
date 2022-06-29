# Nested functions are possible in Python

def test():
    x = 'this is x' # Can accessed by a child function
    
    def test2():
        y = 'this is y' # This is only accessible within test2
        print(x)
        print(y)
    
    test2()
    # print(y) => error
    
# test2() => Error; test2 can only be used with the scope of test
# test.test2() # Will not work
test()

print('\n\n\n')
 
# Passing functions as an argument
def parent_fucntion(func_name):
    func_name()
    
    
def test3():
    print('Hello from test3')


parent_fucntion(test3)

print('\n\n\n')
# Decorators
import random

def sum_array(arr):
    s = 0
    for a in arr:
        s += a
    return s
    # return sum(arr)

def get_int_array_100():
    l = list()
    for i in range(100):
        l.append(random.randint(1,1000))
    return l


def get_int_array_1000():
    l = list()
    for i in range(1000):
        l.append(random.randint(1,1000))
    return l
    

#If I want to return the summation of the lists returned by the 2 functions above every time
results = get_int_array_100()
print(sum_array(results))
    
results = get_int_array_1000()
print(sum_array(results))


#Instead I can use a decorator

def sum_array_2(function_name):
    results = function_name()
    return sum(results)

def sum_array_3(function_name): # Decorator usually take a function as a paremeter
    def wrapper(): #wrapper is not a keyword. but a convention
        results = function_name()
        return sum(results)
    return wrapper

@sum_array_3 # same as sum_array_3(get_int_array_10000)()
def get_int_array_10000():
    l = list()
    for i in range(10000):
        l.append(random.randint(1,1000))
    return l
    # return [random.randint(1,1000) for i in range(10000)]

@sum_array_3
def get_int_array_100000():
    return [random.randint(1,1000) for i in range(100000)]


print('\n\n\n',sum_array_2(get_int_array_1000))
print(get_int_array_10000())