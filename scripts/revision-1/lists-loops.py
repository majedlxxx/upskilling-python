


a = [1,2,3,4]
a[0]
a[1:-1]
a[::-1]
a[1] = 5 # unlike strings we can modify a list by it's index
print(a)

for i in range(0, len(a)):
    print(i, a[i])


print("-----")
    
for item in a:
    print(item)
    
print("-----")
for i, item in enumerate(a):
    print(i, item)
    
#while condition

grid = [
    [1,2],
    [4,5,6],
    [7,8,9]
]

grid[0][0] # 1
grid[1][1] # 5


for row in grid:
    for item in row:
        print(item)
        
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j])
        
        
def get_grid_size(grid):
    #return (rows, columns)
    #assume it's always complete
    max_size = 0
    for row in grid:
        # max_size = max(len(row), max_size)
        if len(row) > max_size:
            max_size = len(row)
    return (len(grid), max_size)

def sum_grid(grid): # some all rows and columns 
    sum = 0
    
    for row in grid:
        for item in row:
            sum += item
    
    for i in range(row):
        for j in range(len(row)):
            sum += grid[i][j]    
            
    return sum


print(get_grid_size(grid))