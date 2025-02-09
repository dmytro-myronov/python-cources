from math_utils import factorial, gcd
from string_utils import to_upper, trim


def main():
    # Demonstration of math_utils functions
    print("Factorial of 5:", factorial(5))
    print("GCD of 36 and 48:", gcd(36, 48))

    # Demonstration of string_utils functions
    print("Uppercase:", to_upper("hello"))
    print("Trimmed text:", trim("   hello world   "))


if __name__ == "__main__":
    main()
