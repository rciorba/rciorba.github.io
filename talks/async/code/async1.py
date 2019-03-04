async def hello(name):
    return f"hello {name}"

async def main():
    print(await hello("pytim"))
    print(await hello("pybalkan"))
