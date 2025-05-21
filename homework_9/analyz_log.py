import re
from collections import Counter
from typing import NoReturn


def analyze_log(log_text: str) -> NoReturn:
    """
    Analyzes the provided log text to count and print the number of occurrences of each IP address.

    Args:
        log_text (str): A string containing log entries.

    Prints:
        Each unique IP address found in the log along with the number of times it appears,
        formatted as "{ip}: {count} запит(ів)".
    """
    ip_list = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', log_text)
    ip_counts = Counter(ip_list)

    for ip, count in ip_counts.items():
        print(f"{ip}: {count} запит(ів)")


log_data = """
2025-03-29 15:59:26,338 - INFO - access from ip: 172.167.1.2 security page!
2025-03-29 15:59:26,338 - INFO - access from ip: 172.167.44.2 security page!
2025-03-29 15:59:26,338 - INFO - access from ip: 172.168.1.2 security page!
2025-03-29 15:59:26,338 - INFO - access from ip: 172.167.5.2 security page!
2025-03-29 15:59:26,338 - INFO - access from ip: 172.167.10.2 security page!
2025-03-29 15:59:26,338 - INFO - access from ip: 172.167.1.2 security page!
"""

analyze_log(log_data)
