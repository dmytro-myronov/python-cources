import asyncio

async def slow_task():
    await asyncio.sleep(14)
    print("Hello world after slow_task")


async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
        print("success")
    except TimeoutError as e:
        print("timed out error")
        print(e)


asyncio.run(main())