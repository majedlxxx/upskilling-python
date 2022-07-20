

class Node:
    def __init__(self, value:int, next_node=None, prev_node=None) -> None:
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        
    def __str__(self) -> str:
        return str(self.value)
    

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.length = 0
        
    def get_tail(self) -> Node: #O(n) can be replaced with a dynamic tail attribute / Not used
        node = self.head
        while node.next_node != None:
            node = node.next_node
        return node
    
    def is_empty(self) -> bool:
        return self.head == None
        #return self.length == 0
        
        
    def append(self, value:int) -> None: #O(1)
        new_node = Node(value, None, self.tail)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_node = new_node
        self.tail = new_node
        
       
        
    def get_ith_element(self, index: int) -> Node: #to simulate a[i] #O(n)
        current_index = 0 #a[3]
        node = self.head
        if self.is_empty():
            raise IndexError("Index out of range")
            
            
        while current_index < index:
            node = node.next_node
            if node == None:
                raise IndexError("Index out of range")
                
            current_index += 1
        return node

    def insert_at(self, index: int, value: int) -> None:
        if self.is_empty():
            if index == 0:
                self.append(value)
            else:
                raise IndexError("Index out of range")
        
        current_index = 0
        node = self.head
        while current_index < index:
            node = node.next_node
            if node == None: # large index
                raise IndexError("Index out of range")
            current_index += 1
            
        
        new_node = Node(value, node.next_node, node)
        node.next_node.prev_node = new_node
        node.next_node = new_node
        

        
        
    def length(self) -> int: #O(n) / not needed because we are using the length attribute
        
        node = self.head
        counter = 0
        while node != None:
            counter += 1
            node = node.next_node
        
        return counter
    
    def pop(self, index=-1) -> int: #O(1) 
        if self.is_empty():
            return
        if self.head is self.tail:
            value = self.head.value
            del self.head
            self.head = self.tail = None
            return value
            
        value = self.tail.value
        self.tail.prev_node.next_node = None
        del self.tail
        return value
        
    def find(self, value: int) -> int:
        """
        this function takes an integer (value) and searches for the integer 
        n in the list and returns it's index or -1 if value is not found
        """
        index = 0
        node = self.head
        
        while node != None:
            if node.value == value:
                return index
            node = node.next_node
            index += 1        
        return -1
    
    def remove(self, value: int) -> None: #O(n)
        node = self.head
        
        while node != None:
            
            if node.value == value:
                if node is self.head:
                    self.head = node.next_node
                    self.head.prev_node = None
                
                elif node is self.tail:
                    self.tail = node.prev_node
                    self.tail.next_node = None
                else:  
                    node.prev_node.next_node = node.next_node
                    node.next_node.prev_node = node.prev_node
                    
                del node
                return
            
            node = node.next_node
    
    def remove_all(self, value: int) -> None:
        node = self.head
        nodes_to_delete = list()
        
        while node != None:
            
            if node.value == value:
                if node is self.head:
                    self.head = node.next_node
                    self.head.prev_node = None
                
                elif node is self.tail:
                    self.tail = self.tail.prev_node
                    self.tail.next_node = None
                else:  
                    node.prev_node.next_node = node.next_node
                    node.next_node.prev_node = node.prev_node
                    
                    
                nodes_to_delete.append(node)
                
            node = node.next_node
                
        for node in nodes_to_delete:
            del node
    
    def __str__(self) -> str:
        results = list()
        node = self.head
        while node != None:
            results.append(node.value)
            node = node.next_node
        return str(results)
    
    def print_reverse(self) -> None:
        results = list()
        node = self.tail
        while node != None:
            results.append(node.value)
            node = node.prev_node
        print(results)
    
    
if __name__ == "__main__":
    l = DoublyLinkedList()
    for i in (3,2,3,52,1,3,5,3,3):
        l.append(i)
        


    # print(l.pop())
    l.remove(1)
    print(l)
    print("Reverse: ", end = " ")
    l.print_reverse()
    l.remove_all(3)
    print(l)
    for i in (1, 15, 20):
        l.append(i)
    print(l)
    l.insert_at(0, 7)
    print(l)
    l.print_reverse()