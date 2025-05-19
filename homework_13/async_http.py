import asyncio
import logging
import aiohttp
from bs4 import BeautifulSoup
from typing import List, Union, Optional
from aiohttp import ClientSession

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)


async def download_page(session: ClientSession, url: str) -> str:
    """
    Загружает страницу по URL, парсит doctype и заголовок страницы.

    Args:
        session (ClientSession): Активная сессия aiohttp.
        url (str): URL страницы для загрузки.

    Returns:
        str: Строка с doctype и заголовком страницы.
    """
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')

        # Получаем doctype из документа, если есть
        doctype: Optional[str] = None
        for item in soup.contents:
            if isinstance(item, type(soup.Doctype)):
                doctype = f"<!DOCTYPE {item}>"
                break

        try:
            title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
        except Exception as e:
            logger.error(f"Error parsing title for {url}: {e}", exc_info=True)
            title = "Can't parse title"

        if doctype:
            logger.info(f"Doctype for {url}: {doctype}")
        logger.info(f"Title for {url}: {title}")

        return f"{doctype or 'No DOCTYPE'} | {title}"


async def fetch_all(session: ClientSession, urls: List[str]) -> List[Union[str, Exception]]:
    """
    Одновременная загрузка нескольких страниц и получение их заголовков и doctype.

    Args:
        session (ClientSession): Активная сессия aiohttp.
        urls (List[str]): Список URL для загрузки.

    Returns:
        List[Union[str, Exception]]: Список результатов загрузки или исключений.
    """
    tasks = [download_page(session, url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results


async def main() -> None:
    """
    Главная функция: создаёт сессию, загружает список URL и выводит результаты.
    """
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://rezka.ag/",
            "https://www.netflix.com/",
            "https://www.google.com/",
            "https://go2.utorr.cc/"
        ]
        results = await fetch_all(session, urls)
        logger.info(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
