async def hello(name):
    return f"hello {name}" # P.S. how cool are format string!?

async def main():
    print(await hello("pytim"))
    print(await hello("pybalkan"))

print(main())
