from multiprocessing import Process
import time

def brew_chai():
    print(f"Starting to brew chai...")
    count = 0
    for _ in range(100_000_000):
        count += 1  # Simulating CPU-bound work
    print(f"Chai is ready!")
    


if __name__ == "__main__":
    
    start = time.time()

    process1 = Process(target=brew_chai)
    process2 = Process(target=brew_chai)


    process1.start()
    process2.start()
    process1.join() 
    process2.join()
    end = time.time()

    print(f"All chai drinks are ready! Time taken: {end - start:.2f} seconds")