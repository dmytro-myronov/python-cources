
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)  # Asynchronously put an item into the queue
        print(f"Produced {i}")
        await asyncio.sleep(1)  # Simulate work


async def consumer(queue):
    while True:
        item = await queue.get()  # Asynchronously get an item
        print(f"Consumed {item}")
        queue.task_done()  # Mark the task as done



async def main():
    queue = asyncio.Queue()

    # Start producer and consumer
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.sleep(6)  # Allow some time for processing
    consumer_task.cancel()  # Stop consumer after a while

# Run the event loop
asyncio.run(main())
