import re
from typing import List

def extract_urls(text: str) -> List[str]:
    """
    Extracts all URLs from the provided text.

    The pattern matches:
    - URLs starting with 'http://' or 'https://'
    - Followed by any characters that are not whitespace, angle brackets, or quotes

    Args:
        text (str): The input string that may contain URLs.

    Returns:
        List[str]: A list of extracted URL strings.
    """
    pattern = r'https?://[^\s<>"]+'
    return re.findall(pattern, text)


# Example usage
text = "Ось сайт: https://example.com і ще один http://test.org/page.html. А це просто текст."
urls = extract_urls(text)
print(urls)
