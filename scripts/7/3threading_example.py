import threading
import random

def sum_list(l):
    s = 0
    for i in l:
        s += i
    
    print(s)
    
    
    
l = [random.randint(1, 500) for i in range(1,1_000_000)]
# s = sum_list(l)
# print(s)
t = threading.Thread(target=sum_list, args=(l,)) #if the function that I am calling takes arguments we send them as a tuple(args)
t.start()