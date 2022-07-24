from queue import Queue
import random
import threading
import time


q = Queue()

DATA_SIZE = 1_000_000

def insert_to_queue():
    for i in range(DATA_SIZE):
        q.put(random.randint(1, 50000))
        
def insert_to_queue_2():
    for i in range(DATA_SIZE//4):
        q.put(random.randint(1, 50000))

def sum_queue():
    sum = 0
    counter = 0 
    while True:
        counter += 1
        if counter == DATA_SIZE:
            break
        sum += q.get()

if __name__ == "__main__":
    starting_time = time.time()
    insert_to_queue()
    print("Done")
    sum_queue()
    print("Done")
    ending_time = time.time()
    without_threading_time = ending_time-starting_time
    
    starting_time = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=insert_to_queue_2)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    sum_queue()
    ending_time = time.time()
    with_threading_time = ending_time-starting_time
    
    print("Without threading: ", without_threading_time)
    print("With threading: ", with_threading_time)
    
        
    