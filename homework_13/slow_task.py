import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)


async def slow_task() -> None:
    """
    Асинхронная задача, которая спит 14 секунд и выводит сообщение.
    """
    await asyncio.sleep(14)
    logger.info("Hello world after slow_task")


async def main() -> None:
    """
    Запускает slow_task с таймаутом 5 секунд.

    Если задача не успевает выполниться за 5 секунд,
    ловит исключение asyncio.TimeoutError и выводит сообщение.
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
        logger.info("success")
    except asyncio.TimeoutError as e:
        logger.error("timed out error")
        logger.debug(e, exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
