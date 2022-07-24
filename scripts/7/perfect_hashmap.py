"""
    Perfect hashmaps only contain 1 item per address/sublist
    This can only be done using some strict rules for example that only numbers between 0 and 999,999 are allowed
    in perfect hashmaps search takes O(1)
"""


# arr = [False, True, False, False, True]
# arr[3] => False which mean that 3 doesn't exist
# insert(1)
# search(1)
# Visited_array


class HashMap: 
    def __init__(self, size = 1_000_000) -> None:
        self.size = size
        self.data = [False for i in range(size)] #Visited array
                
    @staticmethod
    def hash_function(n: int) -> int:
        return n
        
    def insert(self, n: int) -> None: #O(1)
        if n not in range(0, self.size):
            raise ValueError(f"Numbers should be between 0 and {self.size}")
        location = self.hash_function(n)
        self.data[location] = True
        
    def exists(self, n: int) -> None: # O(1)
        location = self.hash_function(n)
        return self.data[location]
    
    
if __name__ == "__main__":
    h = HashMap()
    h.insert(1)
    print(h.exists(1))
    print(h.exists(55))
    