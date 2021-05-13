import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    task3 = asyncio.create_task(
        say_after(4, 'Bobi'))

    task4 = asyncio.create_task(
        say_after(3, 'I am'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2
    await task3
    await task4

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())

