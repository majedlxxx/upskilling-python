import threading
import time




def process_data():
    time.sleep(5)
    print("Done with processing")


    
# process_data() # Without multithreading the interpreter will call the function and wait for it to finish and only then will start working on the code below
# But with threading processing data is done in parallel with the rest of the code
print("Without threading")
start = time.time()
process_data()
process_data()
end = time.time()

print(f"{end - start} seconds")


t = threading.Thread(target=process_data)


print("With threading")
start = time.time()
t = threading.Thread(target=process_data)
t2 = threading.Thread(target=process_data)
t.start()
t2.start()
t.join() # wait for t to finish.
t2.join()
end = time.time()


print(f"{end - start} seconds")