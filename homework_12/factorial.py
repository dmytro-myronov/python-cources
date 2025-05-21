from multiprocessing import Pool
from typing import List, Tuple

import sys
sys.set_int_max_str_digits(10_000_000)


def partial_factorial(range_tuple: Tuple[int, int]) -> int:
    """
    Обчислює добуток чисел в діапазоні [start, end].

    :param range_tuple: Кортеж (start, end), межі діапазону включно.
    :return: Добуток усіх цілих чисел від start до end.
    """
    start, end = range_tuple
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def chunk_ranges(n: int, chunks: int) -> List[Tuple[int, int]]:
    """
    Розбиває інтервал [1, n] на приблизно рівні частини.

    :param n: Верхня межа діапазону.
    :param chunks: Кількість частин для розбиття.
    :return: Список кортежів (start, end) для кожної частини.
    """
    chunk_size = n // chunks
    ranges = []
    start = 1
    for i in range(chunks):
        end = start + chunk_size - 1
        if i == chunks - 1:
            end = n  # останній діапазон до кінця
        ranges.append((start, end))
        start = end + 1
    return ranges

def factorial_parallel(n: int, processes: int = 4) -> int:
    """
    Обчислює факторіал числа n, розподіляючи обчислення між процесами.

    :param n: Число, факторіал якого потрібно обчислити.
    :param processes: Кількість процесів для паралельного обчислення.
    :return: Факторіал числа n.
    """
    ranges = chunk_ranges(n, processes)
    with Pool(processes) as pool:
        partial_results = pool.map(partial_factorial, ranges)
    factorial_result = 1
    for r in partial_results:
        factorial_result *= r
    return factorial_result

if __name__ == "__main__":
    number = 100000
    print("Обчислення факторіалу числа", number)
    result = factorial_parallel(number, processes=8)
    print(f"Довжина факторіалу {number}: {len(str(result))} цифр")
