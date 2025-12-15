import threading
import time


def cpu_heavy():
    print("Starting CPU heavy task...")
    count = 0
    for i in range(10**8):
        count += i
    print("CPU heavy task completed.")
    
    
start = time.time()
thread = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[th.start() for th in thread]
[th.join() for th in thread]
end = time.time()
print(f"Total time taken for CPU heavy tasks: {end - start:.2f} seconds")