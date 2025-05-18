import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import doctest
import number_utils

def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.
    """
    return n % 2 == 0

def factorial(n: int) -> int:
    """
    Обчислює факторіал числа n.

    Підтримує тільки цілі числа >= 0:
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Факторіал визначений лише для невід'ємних цілих чисел
    """
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних цілих чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



