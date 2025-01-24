from collections.abc import Iterable


class Custom:
    """
    A custom class that implements basic operations on iterable objects
    such as calculating the length, sum, and minimum value.
    """

    def my_len(self, iter):
        """
        Custom implementation of the `len` function.

        Args:
            iter (Iterable): The iterable whose length is to be calculated.

        Returns:
            int: The number of elements in the iterable.
        """
        if isinstance(iter, Iterable):
            i = 0
            for x in iter:
                i = i + 1
            return i

    def my_sum(self, iter):
        """
        Custom implementation of the `sum` function.

        Args:
            iter (Iterable): The iterable whose elements are to be summed.

        Returns:
            int: The sum of the elements in the iterable.
        """
        if isinstance(iter, Iterable):
            sum = 0
            for x in iter:
                sum = sum + x
            return sum

    def my_min(self, iter):
        """
        Custom implementation of the `min` function.

        Args:
            iter (Iterable): The iterable from which to find the minimum value.

        Returns:
            The minimum value in the iterable.
        """
        if isinstance(iter, Iterable):
            min = None
            i = 0
            for x in iter:
                if i == 0:
                    min = x
                elif x < min:
                    min = x
                i = i + 1

            return min


# Create an instance of the Custom class
custom = Custom()

# Example usage of the custom methods
l = custom.my_len([4, 6, 7])  # Calculate the length of the list
summ = custom.my_sum([4, 6, 7])  # Calculate the sum of the list
min = custom.my_min([4, 6, 7, 2, 1])  # Find the minimum value in the list

# Print the results
print(l)  # Output: 3
print(summ)  # Output: 17
print(min)  # Output: 1

# Assertions to verify correctness
assert custom.my_min([4, 6, 7, 2]) == 2, "Must be 2"
assert custom.my_sum([4, 6, 7, 2]) == 19, "Must be 19"
assert custom.my_len([4, 6, 7, 2]) == 4, "Must be 4"
