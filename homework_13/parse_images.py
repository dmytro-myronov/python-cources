import asyncio
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
from bs4 import Tag
from urllib.parse import urljoin
import os

async def prepare_images_urls(session, url):
    async with session.get(url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.find_all('img')

        full_images_urls = []
        for i, image_tag in enumerate(images):
            print(f"prepare image {i}")
            if isinstance(image_tag, Tag):
                image_name = image_tag.get('alt') or f"Default_{i}.jpg"
                image_url = image_tag.get('src')
                full_image_url = urljoin(url, image_url)
                full_images_urls.append((image_name, full_image_url))
        return full_images_urls


async def download_image(session, image_tuple):
    image_name, image_url = image_tuple
    print(f"download image {image_name}")

    try:
        async with session.get(image_url) as resp:
            if resp.status == 200:
                async with aiofiles.open(f'images/{image_name}', 'wb') as f:
                    while True:
                        chunk = await resp.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
    except Exception as e:
        print(f"Error downloading {image_name}: {e}")


async def fetch_all(session, urls: list):
    tasks = [download_image(session, url) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def main():
    main_url = "https://go2.utorr.cc/"

    # Ensure 'images' folder exists
    os.makedirs("images", exist_ok=True)

    async with aiohttp.ClientSession() as session:
        urls = await prepare_images_urls(session, main_url)
        await fetch_all(session, urls)

asyncio.run(main())
