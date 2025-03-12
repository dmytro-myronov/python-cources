# News Scraper

This script scrapes news articles from Google News and saves the extracted data into a CSV file.

## Features
- Scrapes news article titles, URLs, publication dates, and image links.
- Allows filtering of articles by a specified time range.
- Saves extracted data into a `news.csv` file.
- Uses `BeautifulSoup` for HTML parsing and `requests` for fetching web pages.

## Prerequisites
Ensure you have Python 3 installed along with the following dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage
Run the script with:

```bash
python parse_news.py
```

You will be prompted to enter a number of hours to filter news articles from recent history. If left empty, all available articles will be retrieved.

## Output
The extracted news data is stored in `news.csv` with the following columns:
- `article_title`
- `article_full_url`
- `article_date_public`
- `image_link`

## Error Handling
- Handles HTTP request failures.
- Skips articles with missing or invalid data.
- Provides user-friendly error messages for incorrect inputs.

## License
This script is provided under the MIT License.
