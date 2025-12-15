import asyncio
import time


async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready!")
    
start = time.time() 
async def main():
    await asyncio.gather(
        brew("coffee"),
        brew("tea"),
        brew("chai")
    )
    
asyncio.run(main())
end = time.time()
print(f"Total time taken to brew all beverages: {end - start:.2f} seconds")