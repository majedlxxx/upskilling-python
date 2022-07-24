"""
    User input:
        list size: n size of list l
        m queries is an item in that the list l
    n integers in the list l

    
"""
n = int(input("Enter the number of integers: "))
# l = list()
l = set()
for i in range(n):
    x = int(input(">> "))
    
    # l.append(x)
    l.add(x)    
    
m = int(input("Enter the number of queries: "))
for i in range(m): # o(n*m) if I was using a list / o(m) if I was using a set
    q = int(input("Enter a number to find: "))
    print(q in l)