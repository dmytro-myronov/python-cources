import asyncio
import logging
import os
from typing import List, Tuple, Union

from aiohttp import ClientSession
import aiofiles
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)


async def prepare_images_urls(session: ClientSession, url: str) -> List[Tuple[str, str]]:
    """
    Получает HTML страницы, парсит все теги <img> и формирует список
    кортежей (имя_изображения, полный_url_изображения).

    Args:
        session (ClientSession): Асинхронная сессия HTTP клиента.
        url (str): URL страницы для парсинга.

    Returns:
        List[Tuple[str, str]]: Список кортежей с именем и URL изображений.
    """
    async with session.get(url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.find_all('img')

        full_images_urls: List[Tuple[str, str]] = []
        for i, image_tag in enumerate(images):
            logger.info(f"prepare image {i}")
            if isinstance(image_tag, Tag):
                image_name = image_tag.get('alt') or f"Default_{i}.jpg"
                image_url = image_tag.get('src')
                if image_url:
                    full_image_url = urljoin(url, image_url)
                    full_images_urls.append((image_name, full_image_url))
        return full_images_urls


async def download_image(session: ClientSession, image_tuple: Tuple[str, str]) -> None:
    """
    Загружает изображение по URL и сохраняет его в папку 'images'.

    Args:
        session (ClientSession): Асинхронная сессия HTTP клиента.
        image_tuple (Tuple[str, str]): Кортеж (имя_изображения, URL_изображения).
    """
    image_name, image_url = image_tuple
    logger.info(f"download image {image_name}")

    try:
        async with session.get(image_url) as resp:
            if resp.status == 200:
                async with aiofiles.open(f'images/{image_name}', 'wb') as f:
                    while True:
                        chunk = await resp.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
            else:
                logger.warning(f"Failed to download {image_name}: HTTP {resp.status}")
    except Exception as e:
        logger.error(f"Error downloading {image_name}: {e}", exc_info=True)


async def fetch_all(session: ClientSession, urls: List[Tuple[str, str]]) -> List[Union[None, Exception]]:
    """
    Запускает асинхронную загрузку всех изображений из списка.

    Args:
        session (ClientSession): Асинхронная сессия HTTP клиента.
        urls (List[Tuple[str, str]]): Список кортежей (имя_изображения, URL_изображения).

    Returns:
        List[Union[None, Exception]]: Результаты выполнения задач (None или Exception).
    """
    tasks = [download_image(session, url) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def main() -> None:
    """
    Основная функция: создает папку 'images', запускает сессию,
    получает ссылки на изображения и загружает их.
    """
    main_url = "https://go2.utorr.cc/"

    os.makedirs("images", exist_ok=True)

    async with ClientSession() as session:
        urls = await prepare_images_urls(session, main_url)
        await fetch_all(session, urls)


if __name__ == "__main__":
    asyncio.run(main())
