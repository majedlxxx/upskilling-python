# stacks use the principle FILO (First in Last out)

# Implementation option 1 (lists):
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
while len(stack): #First element to enter the stack(1) will be the last one to be popped.
    print(stack.pop())
    
# Option 2 (collections):
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

while len(stack):
    print(stack.pop())