from multi_processing import Process
import time


def cpu_heavy():
    print("Starting CPU heavy task...")
    count = 0
    for i in range(10**8):
        count += i
    print("CPU heavy task completed.")
    
if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [th.start() for th in processes]
    [th.join() for th in processes]
    end = time.time()
    print(f"Total time taken for CPU heavy tasks: {end - start:.2f} seconds")