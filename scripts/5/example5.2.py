import random
import time 

l = [random.randint(1, 5000) for i in range(100000)]

# Get a random sample of size 100 from the list, numbers must be unique
# Calculate the time taken to get the sample


#Method one
sample = list()


starting_time = time.time()
counter = 0
while counter < 100:
    random_int = random.choice(l) # or get a random index (0, len(l))
    if random_int not in sample:
        sample.append(random_int)
        counter += 1
        



ending_time = time.time()
print("Method 1 => Time taken: ", ending_time - starting_time , "Seconds")
print(len(sample))



#Method two
sample = set()

starting_time = time.time()

while len(sample)<100:
    sample.add(random.choice(l))
    
ending_time = time.time()

print("Method 2 => Time taken: ", ending_time - starting_time , "Seconds")
print(len(sample))
