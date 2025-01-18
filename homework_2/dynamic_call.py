
def call_function(obj: object ,func_name ,list_params) -> int:
    dir(obj)
    try:
        getattr(obj, func_name) and callable(getattr(obj, func_name))
        count_params = len(getattr(obj, func_name).__code__.co_varnames) - 1  # cause self
        if len(list_params) != count_params:
            print('please provide correct numbers of params')
        else:
            return getattr(obj, func_name)(*list_params)

    except AttributeError as e:
        print("function does not exist")


class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def add(self, a: int, b: int) -> int:
        """
        Adds two integers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Subtracts the second integer from the first.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The result of a minus b.
        """
        return a - b


calc = Calculator()

print(call_function(calc, "add", [10, 5]))  # 15
print(call_function(calc, "subtract", [10, 5]))  # 5
