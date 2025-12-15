from multiprocessing import Process, Queue

def task(queue):
    print("Starting task...")
    queue.put("Hello from process!")
    print("Task completed.")
    
if __name__ == "__main__":
    queue = Queue()
    process = Process(target=task, args=(queue,))
    
    process.start()
    process.join()

    result = queue.get()
    print(f"Received from process: {result}")
    
    
    