import csv
import requests
from bs4 import BeautifulSoup, Tag
from urllib.parse import urlparse
from datetime import datetime, timedelta
from typing import Optional, List, Tuple


def get_element(tag: Tag, search_tag_name: str, attrs: Optional[dict] = None) -> Optional[Tag]:
    """
    Finds and returns the first matching element within a given tag.

    :param tag: The BeautifulSoup tag to search within.
    :param search_tag_name: The tag name to search for.
    :param attrs: Optional dictionary of attributes to filter by.
    :return: The found Tag object or None if not found.
    """
    try:
        return tag.find(search_tag_name, attrs or {})
    except Exception as e:
        print(f"Error finding element {search_tag_name}: {e}")
        return None


def add_new_film_data(news: List[Tuple[str, str, str, str]]) -> None:
    """
    Appends new film data to a CSV file.

    :param news: A list of tuples containing news data (title, full URL, date published, image link).
    """
    if news:
        with open('news.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['article_title', 'article_full_url', 'article_date_public', 'image_link'])
            writer.writerows(news)
            print("Film data added successfully.")


def parse_news(url: str, date_from: Optional[datetime] = None) -> List[Tuple[str, str, str, str]]:
    """
    Parses news articles from the given URL and extracts relevant data.

    :param url: The URL of the news page.
    :param date_from: Optional datetime to filter articles published after this date.
    :return: A list of tuples containing article title, full URL, date published, and image link.
    """
    response = requests.get(url)
    news_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')  # lxml can be used for better performance
        news_articles = soup.find_all('article', {'class': 'IBr9hb'})
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        for i, article in enumerate(news_articles):
            print(f"Processing article {i}")
            if not isinstance(article, Tag):
                continue

            # Extract publication date
            article_date_element = get_element(article, 'time', {'class': 'hvbAAd'})
            article_date_public = article_date_element.attrs.get('datetime', "") if article_date_element else ""

            try:
                if date_from and article_date_public:
                    published_date = datetime.strptime(article_date_public, "%Y-%m-%dT%H:%M:%SZ")
                    if published_date < date_from:
                        continue
            except ValueError:
                print(f"Failed to parse date for article {i}")
                continue

            # Extract title, link, and image
            title_element = get_element(article, 'a', {'class': 'gPFEn'})
            article_title = title_element.text.strip() if title_element else f"Default_{i}"

            link_element = get_element(article, 'a', {'class': 'WwrzSb'})
            article_full_url = f"{base_url}{link_element.attrs['href']}" if link_element else ""

            image_element = get_element(article, 'img')
            image_link = f"{base_url}{image_element['src']}" if image_element else f"None_{i}"

            news_data.append((article_title, article_full_url, article_date_public, image_link))

    else:
        print(f"Error fetching news page, status code: {response.status_code}")

    return news_data


if __name__ == "__main__":
    main_url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    try:
        hours_input = input("Show the news for the last X hours (provide a number or leave empty): ")
        past_time = datetime.now() - timedelta(hours=int(hours_input)) if hours_input else None
    except ValueError:
        past_time = None
        print("Invalid input. Please enter an integer value for hours.")

    news_list = parse_news(main_url, past_time)
    add_new_film_data(news_list)
