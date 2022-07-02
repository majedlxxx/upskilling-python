'''
    a b c
    d e f
    h i j
    some of the methods below can be either class or static methods. remove self and replace accordingly
'''
'''
    Normal Methods usually deal with an object using the self parameter
    Class Methods => Usually deals with the class itself mainly to get new objects from that class
    Static Method => won't deal with a specific object or the class itself
'''


class Row: # [a,b,c]
    def __init__(self):
        self.data = list()
    
    def add_value_to_row(self, value):
        assert isinstance(value, str) and len(value) == 1, "value must be a single charecter"
        self.data.append(value)
    
    def remove_value_from_row(self, value):
        self.data.remove(value)
    
    @classmethod
    def row_from_list(cls, items):
        new_row = cls()
        for item in items:
            new_row.add_value_to_row(item)
        return new_row
    
    def __str__(self):
        return " ".join(self.data)
    
    
    
class Grid:
    def __init__(self):
        self.rows = list()
    
    def add_row(self, row):
        self.rows.append(row)
        
    def remove_row(self, index):
        self.rows.pop(index)
        
    def all_rows_are_equal():
        """
            Returns True of all rows have the same length
        """
        pass
    
    def square_grid():
        """
            This function return True if the grid is square and False otherwise
            Square grid examples:
                a b
                c d
                
                
                a b c
                d e f
                h i j
                
            None square grids:
                a b
                c
                
                a b c
                d e f
                
            
            
            
        """
        pass
        
    @classmethod
    def grid_from_lists(cls, grid_list):
        """
            receives a 2d list
            [
                ['a', 'b', 'c'],
                ['d', 'e', 'f']
            ]
            returns a gird with the above rows implmented
        """
        new_grid = cls()
        for row_list in grid_list:
            new_row = Row.row_from_list(row_list)
            new_grid.add_row(new_row)
            
        return new_grid
    
    def __str__(self):
        results = ""
        for row in self.rows:
            results += f"{str(row)}\n"
        return results.strip('\n')
        



if __name__ == "__main__":
    r1 = Row()
    r1.add_value_to_row('a')
    r1.add_value_to_row('b')
    r1.add_value_to_row('c')
    r1.add_value_to_row('d')
    r1.remove_value_from_row('d')
    # print(r1)
    
    r2 = Row.row_from_list(['d', 'e', 'f'])
    # print(r2)
    r3 = Row.row_from_list(['h', 'i', 'j'])
    # print(r3)
    
    g1 = Grid()
    
    g1.add_row(r1)
    g1.add_row(r1)
    g1.add_row(r2)
    g1.add_row(r3)
    g1.remove_row(1)
    print(g1)
    
    
    grid_list = [
        ['l', 'm', 'n'],
        ['o', 'p', 'q'],
        ['r', 's', 't']
    ]
    g2 = Grid.grid_from_lists(grid_list)
    print("\n-----\n")
    print(g2)
    
    
    
    
'''
    Modify the above and add necessary classes to do the following:
    1. complete the above functions
    2. there can be 2 types of grids/rows int based or charectar based
    1 3 2
    3 1 4
    2 3 5
    
    a b c
    c e f
    g h i 
 
'''