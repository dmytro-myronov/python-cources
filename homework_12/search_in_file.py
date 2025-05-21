import concurrent.futures
from typing import List, Tuple

def search_in_file(filename: str, search_text: str) -> Tuple[str, List[Tuple[int, str]]]:
    """
    Шукає рядки з текстом `search_text` у файлі `filename`.

    Args:
        filename (str): Шлях до файлу.
        search_text (str): Текст, який шукаємо.

    Returns:
        Tuple[str, List[Tuple[int, str]]]: Кортеж з іменем файлу та списком знайдених рядків.
            Кожен елемент списку — кортеж з номера рядка та тексту рядка.
    """
    found_lines: List[Tuple[int, str]] = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for lineno, line in enumerate(f, start=1):
                if search_text in line:
                    found_lines.append((lineno, line.strip()))
        return filename, found_lines

    except FileNotFoundError as e:
        print(e)


def main(files: List[str], search_text: str) -> None:
    """
    Паралельно шукає `search_text` у списку файлів `files` і виводить результати.

    Args:
        files (List[str]): Список шляхів до файлів.
        search_text (str): Текст для пошуку.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_in_file, file, search_text) for file in files]
        for future in concurrent.futures.as_completed(futures):
            filename, results = future.result()
            print(f"\nРезультати пошуку у файлі {filename}:")
            if results:
                for lineno, line in results:
                    print(f"  рядок {lineno}: {line}")
            else:
                print("  Текст не знайдено.")

if __name__ == "__main__":
    files = ["file1.txt", "file2.txt"]
    search_text = input("текст для пошуку: ")
    main(files, search_text)
