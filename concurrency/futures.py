import asyncio

async def normal_func():
    print("this is before the normal function")
    print("this is after the normal function")

async def function1():
    print("this is before the function")
    await asyncio.sleep(1)
    print("this is after the function")

async def function2():
    print("this is before the function")
    await asyncio.sleep(1)
    print("this is after the function")

async def main():
    asyncio.create_task(normal_func())
    # await asyncio.create_task(function2())
    await asyncio.gather(function1(), function2())


if __name__ == "__main__":
    asyncio.run(main())
