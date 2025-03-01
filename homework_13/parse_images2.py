import asyncio
from bs4 import BeautifulSoup
import requests
from bs4 import Tag



async def prepare_images_urls(url):
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    i = 0
    full_images_urls = []
    for image_tag in images:
        print(f"try download image {i}")
        if isinstance(image_tag, Tag):
            image_name = image_tag.get('alt') if image_tag.get('alt') else f"Default_{i}"
            image_url = image_tag.get('src')
            full_images_urls.append((image_name,url + image_url))
        i += 1

    return full_images_urls








async def download_page(url: str):
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    images  =soup.find_all('img')
    i = 0
    full_images_urls = []
    for image_tag in images:
        print(f"try download image {i}")
        if isinstance(image_tag, Tag):
            image_name = image_tag.get('alt') if image_tag.get('alt') else f"Default_{i}"
            image_url = image_tag.get('src')
            full_images_urls.append(url + image_url)
            with open('images/' + image_name, 'wb') as file:
                response = requests.get(url + image_url, stream=True)
                if response.status_code == 200:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
        i+=1

    return req.text


async def main(url: str):
    html_data = await download_page(url)
    print("images downloaded")

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




asyncio.run(main("https://go2.utorr.cc/"))






