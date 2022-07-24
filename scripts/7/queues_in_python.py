# Queues use the FIFO(First in First out)

# Implementation option 1 (lists):
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
while len(queue): #First element to enter the queue will be the first one to get out of it.
    print(queue.pop(0))
    
# Option 2 (collection)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

while len(queue):
    print(queue.popleft())

# Option 3 (Queue) / fastest /best choice
from queue import Queue
q = Queue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty(): #we are using .empty method because len won't work here
    print(q.get())