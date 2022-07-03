# assert is mainly used for input validation
'''
assert condition
assert condition, optional_message
'''



def devide(a ,b):
        
        
    assert type(a) == int, "a must be an integer"
    assert isinstance(b, int), "b must be an integer"
    assert b != 0, "b must not be equal to zero"
    return a/b
    
    # if type(a) != int:
    #     raise TypeError('A must be an integer')
    
        # raise Exception('A must be an integer')
        
        
    # try:
    #     return a/b
    # except TypeError as e:
    #     print(e)


print(devide("test",2))
print("After the function call")
#assert x == 'test' , 'X is not test'