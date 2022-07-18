


class Node:
    def __init__(self, value:int, next_node = None) -> None:
        self.value = value
        self.next_node = next_node
        
    def __str__(self) -> str:
        return str(self.value)
        
        

class ConventionalList: #singly linked list
    """
    head => first element in the list
    tail => last element in the list
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        
    def get_tail(self) -> Node: #O(n) can be replaced with a dynamic tail attribute
        node = self.head
        while node.next_node != None:
            node = node.next_node
        return node
    
    def is_empty(self) -> bool:
        return self.head == None
        
        
        
    def append(self, value:int) -> None: #O(1)
        new_node = Node(value)
        if self.is_empty(): #empty list
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
        """
        1 => 3 => 6 => 15 => 20 => None
        insert_at(2, 30)
        
        1 => 3 => 30 => 6 => 15 => 20 => None
        
        Odd cases:
        large index
        empty list
        
        """
        
        if self.is_empty():
            if index == 0:
                self.append(value)
            else:
                raise IndexError("Index out of range")
        
        current_index = 0
        node = self.head
        while current_index < index - 1:
            node = node.next_node
            if node == None: # large index
                raise IndexError("Index out of range")
            current_index += 1
        prev_node = node #3
        next_node = node.next_node #6
        new_node = Node(value, next_node) #30
        prev_node.next_node = new_node
        
        
    def length(self) -> int: #O(n)
        
        node = self.head
        counter = 0
        while node != None:
            counter += 1
            node = node.next_node
        
        return counter
    
    def pop(self, index=-1) -> int: #O(n) 
        """
            Removes the last node and returns it's value
            -1 => remove last else remove indexth node
            
        """
        #1 => 2 => 5(new tail) => 7(current tail) => None
        if self.is_empty():
            return
        if self.head == self.tail: #one element in the list
            value = self.head.value
            del self.head
            self.head = self.tail = None
            return value
            
        node = self.head
        while node.next_node is not self.tail:
            node = node.next_node
                        
        new_tail = node
        new_tail.next_node = None
        value = self.tail.value
        del self.tail
        self.tail = new_tail
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
    
    def remove(self, value: int) -> None:
        """
            Replicate python's list remove behaviour 
            remove the first instance of that value
            or raise a value error if the value does not exist
        """
        
        prev = None
        node = self.head
        
        while node != None:
            
            if node.value == value:
                prev.next_node = node.next_node
                del node
                return
            
            # odd case head/tail
            
            prev = node
            node = node.next_node
    
    def remove_all(self, value: int) -> None:
        """
            same as the above but remove all instances
        """
        pass
        
                
            
    
    
if __name__ == "__main__":
    l = ConventionalList()
    # l.append(1)
    print("Length: ",l.length())
    #1 => 3 => 6 => 15 => 20
    for i in (1, 3, 6, 15, 20):
        l.append(i)

    print("Length: ",l.length())
    l.insert_at(2, 30)
    print("Length after insertion: ",l.length())

    node = l.head
    while node != None:
        print(node)
        node = node.next_node
        
    exit()

    print("After popping")
    l.pop()
    l.pop()
    node = l.head
    while node != None:
        print(node)
        node = node.next_node
        
        