import asyncio
from typing import List
import aiohttp

async def download_page(session,url: str) -> str:
    """
    Скачивает страницу по URL с помощью requests.

    Args:
        url (str): URL страницы для скачивания.

    Returns:
        str: Текст HTML страницы.
    """

    async with session.get(url) as response:
        return await response.text()


async def main(urls: List[str]) -> None:
    async with aiohttp.ClientSession() as session:
        """
        Асинхронно запускает скачивание страниц по списку URL.
    
        Args:
            urls (List[str]): Список URL для загрузки.
    
        Поведение:
            Для каждого URL создаёт асинхронную задачу скачивания,
            ждёт 5 секунд, затем скачивает и выводит содержимое страницы.
        """
        for url in urls:
            await asyncio.sleep(5)
            html_data = await download_page(session, url)
            print(html_data)


asyncio.run(main([
    "https://rezka.ag/",
    "https://go2.utorr.cc/"
]))
