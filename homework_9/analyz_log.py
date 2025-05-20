import re
from collections import Counter


def analyze_log(log_text):
    # Знаходимо всі IP-адреси в логах
    ip_list = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', log_text)

    # Рахуємо кількість кожної IP
    ip_counts = Counter(ip_list)

    # Виводимо статистику
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

