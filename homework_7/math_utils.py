# math_utils.py

def divide(a: int, b: int) -> float:
    """
    Ділить два числа a на b.

    >>> divide(10, 2)
    5.0
    >>> divide(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
