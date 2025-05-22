import threading
import requests
from typing import List, Tuple


def download_file(url: str, filename: str) -> None:
    """
    Завантажує файл з вказаної URL-адреси та зберігає його під заданим ім'ям.

    Args:
        url (str): URL-адреса файлу для завантаження.
        filename (str): Ім’я файлу, під яким буде збережено завантажений вміст.
    """
    try:
        print(f"[+] Починається завантаження: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Підніме виняток, якщо статус-код != 200

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"[✓] Завершено: {filename}")
    except Exception as e:
        print(f"[✗] Помилка при завантаженні {url}: {e}")


files_to_download: List[Tuple[str, str]] = [
    ("https://go3.utorr.cc/uploads/posts/2025-05/1747558116_poster-954e90e813.jpg", "file1.jpg"),
    ("https://go3.utorr.cc/uploads/posts/2021-10/1638953232_poster-1228254.jpg", "file2.jpg"),
    ("https://go3.utorr.cc/uploads/posts/2024-02/1707878921_poster-b2b3abcd50.jpg", "file3.jpg"),
]

threads: List[threading.Thread] = []
for url, filename in files_to_download:
    t = threading.Thread(target=download_file, args=(url, filename))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("✅ Усі файли завантажено.")
