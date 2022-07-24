# Simplest implementation of a hashmap is to have an array of lists / or in python list of lists
# The main idea behind a hashmap it to distribute you data amongst several lists(arrays)
# Each item can be only found in one sub list(based on a hash function)



import random
import time

class HashMap:
    
    def __init__(self) -> None:
        # self.lists = list()
        # for i in range(10):
        #     self.lists.append(list())
        
        self.lists = [list() for i in range(10)]
    
    @staticmethod
    def hash_function(n: int) -> int:
        """
            To determine the sub list to which n should be added
        """
        return n % 10 # 10 possible outcomes [0-9] inclusive which means we need 10 sub lists
    
    def print_hashMap(self) -> None:
        for i, l in enumerate(self.lists):
            print(f"{i}: {l}")
            
    def insert(self, n: int) -> None: #O(1)
        location = self.hash_function(n)
        self.lists[location].append(n)
    
    def exists(self, n: int) -> bool: #O(M) where m is the length of the sublist
        location = self.hash_function(n)
        for i in self.lists[location]:
            if i == n:
                return True
            
        return False
            
    def clear(self) -> None:
        for l in self.lists:
            l.clear()
        
        
if __name__ == "__main__":
    h = HashMap()
    
    h.insert(5)
    h.insert(7)
    h.insert(105)
    h.insert(77)
    h.insert(3)
    h.insert(22)
    h.print_hashMap()
    print(h.exists(5))
    print(h.exists(99))
    
    h.clear()
    
    #list vs hashmap
    l = list()
    h.clear()
    
    for i in range(1_000_000):
        new_number = random.randint(1,5_000_000)
        l.append(new_number)
        h.insert(new_number)
        
    #List
    to_find = 555
    start = time.time()
    for i in l:
        if i == to_find:
            print("Found in list")
            break
        
    end = time.time()
    print(f"Searching in list took {end-start} seconds")
    
    start = time.time()
    print(h.exists(to_find))
    end = time.time()
    print(f"Searching in hash map took {end-start} seconds")
    