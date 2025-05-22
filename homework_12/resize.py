import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from typing import List


def process_image(image_path: str, output_folder: str = "output", size: tuple = (50, 50)) -> None:
    """
    Змінює розмір зображення та зберігає його в нову папку.

    Args:
        image_path (str): Шлях до вхідного зображення.
        output_folder (str): Папка, куди зберігати оброблені зображення.
        size (tuple): Розмір, до якого змінити зображення (ширина, висота).
    """
    try:
        os.makedirs(output_folder, exist_ok=True)
        img = Image.open(image_path)
        img = img.resize(size)
        base_name = os.path.basename(image_path)
        output_path = os.path.join(output_folder, base_name)
        img.save(output_path)
        print(f"[✓] Оброблено: {base_name}")
    except Exception as e:
        print(f"[✗] Помилка обробки {image_path}: {e}")


def process_images_concurrently(image_paths: List[str]) -> None:
    """
    Обробляє список зображень паралельно за допомогою потоків.

    Args:
        image_paths (List[str]): Список шляхів до зображень.
    """
    with ThreadPoolExecutor() as executor:
        for path in image_paths:
            executor.submit(process_image, path)


if __name__ == "__main__":
    # 🔻 Приклад вхідних зображень (замініть на ваші шляхи)
    images = [
        "file1.jpg",
        "file2.jpg",
        "file3.jpg"
    ]

    process_images_concurrently(images)
    print("✅ Усі зображення оброблено.")
