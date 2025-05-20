import re

def remove_html_tags(html):
    l = re.findall(r"</?[A-Za-z0-9._%+-]*>", html)
    return l


print(remove_html_tags("<html><head></head><body></body></html>values"))