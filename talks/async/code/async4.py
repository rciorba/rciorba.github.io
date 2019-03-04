# since 3.6 you can use yield in coroutines

async def async_generator():
    for n in range(10):
        yield n

async def main():
    async for n in async_generator():
        print(n)
