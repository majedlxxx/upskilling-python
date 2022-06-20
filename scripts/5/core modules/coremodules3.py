import time
from datetime import datetime
import random

epoch_time = time.time() # get the current time in seconds since the epoch(1st of January 1970)

# time.sleep(5) # sleep for 5 seconds


now = datetime.now()
'''
%m => month
%d => day
%Y => year
%H => hour
%M => minute
%S => second

%m/%d/%Y, %H:%M:%S
'''

now = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(now)




# Print the current time every minute

l = []

starting_time = time.time()
for i in range(10000000):
    l.append(random.randint(1,10000))
ending_time = time.time()
print("Time to fill the list: ", ending_time - starting_time)
# l = [random.randint(1,50000000) for i in range(100000)]

starting_time = time.time()
print(5720 in l)
ending_time = time.time()
print("List  => Time taken: ", ending_time - starting_time , "Seconds")


s = set(l)

starting_time = time.time()
print(5720 in s)
ending_time = time.time()

print("Set => Time taken: ", ending_time - starting_time , "Seconds")
exit()

while True:
    now = datetime.now()
    print(now.strftime("%d/%m/%Y, %H:%M"))
    time.sleep(60)
