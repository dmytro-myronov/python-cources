import types


def log_methods(func):
    def wrapper(self, *args, **kwargs):
        print(f"Метод {func.__name__} вызывается.")
        return func(self, *args, **kwargs)

    return wrapper


class MyClass:
    """
    A sample class to demonstrate the log_methods decorator.
    It contains methods for basic arithmetic operations.
    """

    @log_methods
    def add(self, a, b):
        """
        Adds two numbers.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The sum of a and b.
        """
        return a + b

    @log_methods
    def subtract(self, a, b):
        """
        Subtracts the second number from the first.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The result of a - b.
        """
        return a - b


# Testing the class
obj = MyClass()
sum = obj.add(5, 3)
print(sum)
sum2 = obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
print(sum2)
