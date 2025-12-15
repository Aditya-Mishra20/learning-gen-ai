import asyncio
import time

async def boil():
    print("Boiling water...")
    await asyncio.sleep(3)
    print("Water boiled.")
    
asyncio.run(boil())
