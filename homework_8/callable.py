
from typing import Callable

def square(x: int) -> int:
    return x ** 2

def double(x: int) -> int:
    return x * 2

def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    return operation(x)

print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10