import time

def search(l: list, n: int) -> int:
    """
    this function takes a list (l) and an integer (n) and searches for the integer 
    n in l and returns it's index or -1 if n is not found
    """
    operations = 0
    for i in range(len(l)):
        operations += 1
        if l[i] == n:
            return i
    print("Linear search operations:", operations)
    return -1 # Not found




def binary_search(l: list, n: int) -> int: #O(log2(n))
    """
    Binary search only works with sorted lists
    this function takes a list (l) and an integer (n) and searches for the integer 
    n in l and returns it's index or -1 if n is not found
    """
    operations = 0
    low = 0
    high = len(l) - 1
    mid = int(high  / 2)
    while high > low:
        operations += 1
        if n == l[mid]:
            return mid
        elif n > l[mid]:
            low = mid + 1

        else: # n < l[mid]
            high = mid -1

        mid = int(low + (high - low)/2)
    print("Binary search operations: ", operations)
    return -1



# O(n) where n is the list's length
l = [i for i in range(1, 10_000_000)]  # underscores can be used with integers for readability the don't have any affect on the integer's value

start = time.time()
print(search(l, 10_000_000)) #Worst case scenario we had to iterate all 10 million elements to know that the requested number doesn't exist
# We had to do 10 million comparison operations to know if the requested integer doesn't exist
end = time.time()
print(f"Linear search took {end-start} seconds")
# Check theory for Big O notation

start = time.time()
print(binary_search(l, 20_000_000))
end = time.time()
print(f"Binary search took {end-start} seconds")

# l = list()
# for i in range(10_000_000):
#     l.append(i)


exit()
def find_common(a_list: list, b_list: list) -> list:
    """
        this function takes two lists a and b and returns a new 
        list with the common values that are found in both a and b
    """
    results = list()
    for a in a_list:
        for b in b_list:
            if a == b:
                results.append(a)
    
    return results



a = [1,2,3] # 3
b = [2,3,4,5] # 4
# The above function has O(n * m) where n is the length of a and m is the length of b
print(find_common(a, b))


# for i in range(10000): # O(1) Fixed number of operations
#     print(i)


def bubble_sort(l: list): #o(n^2) n is the list's length
    for i in range(len(l) -1):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l


a = [7, 5, 3, 2, 1]
print(bubble_sort(a))

###########
# for i in a: # O(n)
#     print(i)
##########
# for i in a: # (n^2)
#     for j in a:
#         print(i+j)
##########
# for i in a: #O(n)
#     print(i)
# for i in a: #O(n)
#     print(i+1)

# n + n = 2n

#########

# If we want to combine all the above loops in one algorithm:
# n + n^2 + 2n = 3n + N^2 => We ignore the smaller notation => N^2

# for i in range(int(len(a)/2)): # O(1/2N) => we ignore multiples so we say O(N)
#     print(a[i])





