import asyncio

class Cache:
    def __init__(self):
        self.lock = asyncio.Lock()
        self.cache = {}

    async def get(self, key):
        async with lock:
            self.cache.get(key)

    async def set(self, key, value):
        async with lock:
            self.cache[key] = value
        

