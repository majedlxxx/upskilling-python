class CappedSizeList:
    
    def __init__(self, size = 3):
        self.size = size
        self.data = list()
        
    def append(self, value):
        self.data.append(value)
        if len(self.data) > self.size:
            self.data.pop(0)
        
    def __str__(self):
        return str(self.data)
    
    def values(self):
        return self.data
    
    
# x = CappedSizeList(3)
# items = [1,2,3,4,5,6]

# for item in items:
#     x.append(item)
#     print(x)
#     input("continue")



#without class
# a = [1,2,3]
# items = [4,5,6]

# for item in items:
#     a.append(item)
#     a.pop(0)
#     print(a)
#     input("Continue")

items = [1,2,3,4]

for item in items:
    print(item)
    items.pop(0)
    items.append(5)
   
for item in items:
    items.append(1)
    
print(items)
"""

items = [1,2,3,4]
item => point at the first element in the array (1)
items = [2,3,4,5]
item => points at the second element in the array(3)
#2 was skipped, if it's needed for any purpose you have discarded it.



"""



print(items)
    