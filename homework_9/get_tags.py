import re
from typing import List

def get_all_tags(text: str) -> List[str]:
    """
    Extracts all hashtags from the given text.

    A hashtag is defined as a '#' followed by any combination of letters, digits,
    dots, underscores, percent signs, plus, or hyphens.

    Args:
        text (str): The input string containing hashtags.

    Returns:
        List[str]: A list of hashtags found in the text.
    """
    tags = re.findall(r"#[A-Za-z0-9._%+-]*", text)
    return tags


# Example usage
print(get_all_tags("Enter the text:#tag1,#tag2,#tag3,#newfilm: "))
