import re

def extract_urls(text) -> list:
    # Регулярний вираз для пошуку URL
    pattern = r'https?://[^\s<>"]+'
    return re.findall(pattern, text)

text = "Ось сайт: https://example.com і ще один http://test.org/page.html. А це просто текст."
urls = extract_urls(text)
print(urls)
