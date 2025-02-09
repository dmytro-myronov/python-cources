
import math

def factorial(n):
    """Computes the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative numbers")
    return math.factorial(n)


def gcd(a, b):
    """Finds the greatest common divisor of two numbers."""
    return math.gcd(a, b)

