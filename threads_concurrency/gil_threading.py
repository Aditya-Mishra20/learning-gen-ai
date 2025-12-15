import threading
import time


def brew_chai():
    print(f"{threading.current_thread().name} - Starting to brew chai...")
    count = 0
    for _ in range(100_000_000):
        count += 1  # Simulating CPU-bound work
    print(f"{threading.current_thread().name} - Chai is ready!")
    

thread1 = threading.Thread(target=brew_chai, name =" chai_maker_1")
thread2 = threading.Thread(target=brew_chai, name =" chai_maker_2")


start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join() 
end = time.time()

print(f"All chai drinks are ready! Time taken: {end - start:.2f} seconds")


