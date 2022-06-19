from unittest import result
from mathops import add, multiply

def sum_list(l): # [1,2,3] = > 6
    #don't use "+" use the add function from mathops instead
    sum = 0
    for i in l:
        sum = add(sum, i)
    return sum

def multiply_list(l):# [4,5,2] => 40
    #don't use "*" use the multiply function from mathops instead
    results = 1
    for i in l:
        results = multiply(results,i)
    return results

print(sum_list([1,2,3]))
print(multiply_list([4,5,2]))


