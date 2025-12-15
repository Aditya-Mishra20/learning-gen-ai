import threading
import time



def boil_water():
    print("Boiling water...")
    time.sleep(5)
    print("Water boiled.")
    
def brew_chai():
    print("Brewing chai...")
    time.sleep(3)
    print("Chai is ready!")
    
# creating threads
boil_thread = threading.Thread(target=boil_water)
brew_thread = threading.Thread(target=brew_chai)

start = time.time()
boil_thread.start()
brew_thread.start()
#wait for both threads to complete
brew_thread.join()
boil_thread.join() # join means wait here until this thread completes
end = time.time()
print(f"Time taken: {end - start:.2f} seconds")
