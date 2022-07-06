
def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: # i % 15 == 0
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
    


n = 15
fizzBuzz(n)

'''
given n(integer)
i: 1 => n(inclusively)
and for each i print:
    fizz if the number is a multiple of 3
    buzz if the number is a multiple of 5
    fizzbuzz if the number is a multiple of both 3 and 5
    i if the number can not be divided by 3 or 5

'''
