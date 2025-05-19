import asyncio
from asyncio import Queue
from typing import NoReturn


async def producer(queue: Queue[int]) -> None:
    """
    Асинхронный производитель, который кладет элементы в очередь.

    Args:
        queue (Queue[int]): Асинхронная очередь для передачи данных.
    """
    for i in range(5):
        await queue.put(i)  # Асинхронно кладем элемент в очередь
        print(f"Produced {i}")
        await asyncio.sleep(1)  # Симуляция работы


async def consumer(queue: Queue[int]) -> NoReturn:
    """
    Асинхронный потребитель, который получает элементы из очереди бесконечно.

    Args:
        queue (Queue[int]): Асинхронная очередь для получения данных.
    """
    while True:
        item = await queue.get()  # Асинхронно получаем элемент из очереди
        print(f"Consumed {item}")
        queue.task_done()  # Отмечаем задачу как выполненную


async def main() -> None:
    """
    Основная функция для запуска производителя и потребителя.

    Создает очередь, запускает задачи производителя и потребителя,
    ожидает 6 секунд и отменяет задачу потребителя.
    """
    queue: Queue[int] = asyncio.Queue()

    # Запускаем производителя и потребителя
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.sleep(6)  # Даем время на обработку
    consumer_task.cancel()  # Останавливаем потребителя
