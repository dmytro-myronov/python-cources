import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def download_page(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            #print("Status:", response.status)
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(soup.title.string)
            return soup.title.string


async def fetch_all(urls: list):
    tasks = [download_page(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True) #????
    return results


async def main():
    urls = [
        "https://rezka.ag/",
        "https://www.netflix.com/",
        "https://www.google.com/",
        "https://go2.utorr.cc/"
    ]
    results = await fetch_all(urls)
    print(results)

asyncio.run(main())