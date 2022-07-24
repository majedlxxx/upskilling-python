"""
    Sets and dictionaries are built on top of hashmaps in python
"""

import random
import time
size = 1_000_000
l = list()
d = dict()
s = set()

start = time.time()
for i in range(size):
    l.append(i)
end = time.time()
print(f"Filling the list with {size} integers took {end - start} seconds")


start = time.time()
for i in range(size):
    d[i] = i
end = time.time()
print(f"Filling the dictionary with {size} integers took {end - start} seconds")


start = time.time()
for i in range(size):
    s.add(i)
end = time.time()
print(f"Filling the set with {size} integers took {end - start} second")

# {
#     1:1,
#     7:7
# }


    


l = [random.randint(1, 50_000_000) for i in range(size)]
s = set(l)
d = dict()
for i in l:
    d[i] = i

start = time.time()
print(5 in l)
end = time.time()
print(f"Search took {end - start} seconds using lists")


start = time.time()
print(5 in s)
end = time.time()
print(f"Search took {end - start} seconds using sets")


start = time.time()
print(5 in d)
end = time.time()
print(f"Search took {end - start} seconds using dictionary")