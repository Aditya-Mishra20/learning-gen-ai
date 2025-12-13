from multiprocessing import Process
import time


def brew_coffee(chai):
    print(f"Starting to brew {chai} chai...")
    time.sleep(3)
    print(f"{chai} chai is ready!")
    
    
if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_coffee, args=(f"drink maker {i+1}",)),
        for i in range(3)
    ]