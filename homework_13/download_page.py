import asyncio

import requests


async def download_page(url: str):
    req = requests.get(url)
    return req.text


async def main(urls: list):
    for url in urls:
        asyncio.create_task(download_page(url))
        await asyncio.sleep(5)
        html_data = await download_page(url)
        print(html_data)


asyncio.run(main([
    "https://rezka.ag/",
    "https://go2.utorr.cc/"
]))
