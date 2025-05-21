import re
from typing import List

def remove_html_tags(html: str) -> List[str]:
    """
    Extracts HTML tags from the input string.

    The pattern matches:
    - Opening and closing HTML tags (e.g., <tag>, </tag>)
    - Tags may include letters, digits, dots, underscores, percent, plus, or hyphens.

    Args:
        html (str): The input HTML string.

    Returns:
        List[str]: A list of matched HTML tags.
    """
    tags = re.findall(r"</?[A-Za-z0-9._%+-]*>", html)
    return tags


# Example usage
print(remove_html_tags("<html><head></head><body></body></html>values"))
