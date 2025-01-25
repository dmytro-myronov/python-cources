import math


class Vector:
    """
    A class to represent a mathematical vector and perform operations such as addition,
    subtraction, comparison, and multiplication based on vector lengths.

    Attributes:
        components (tuple): The components of the vector.
    """

    def __init__(self, *components):
        """
        Initializes a Vector object with the given components.

        Args:
            *components: The components of the vector (e.g., x, y, z coordinates).
        """
        self.components = components

    def validation(self, vector_obj):
        """
        Validates if the given object is a Vector and has the same dimensions.

        Args:
            vector_obj (Vector): The vector object to validate.

        Raises:
            ValueError: If the object is not a Vector or dimensions do not match.
        """
        if not isinstance(vector_obj, Vector):
            raise ValueError("Please use a Vector object")
        if len(self.components) != len(vector_obj.components):
            raise ValueError("Vectors must have the same dimensions")

    def __add__(self, other):
        """
        Calculates the sum of the lengths of two vectors.

        Args:
            other (Vector): The vector to add.

        Returns:
            float: The sum of the lengths of the two vectors.

        Raises:
            ValueError: If the other object is not a Vector or dimensions do not match.
        """
        self.validation(other)
        n2 = math.sqrt(sum(x ** 2 for x in other.components))
        n1 = math.sqrt(sum(x ** 2 for x in self.components))
        return n1 + n2

    def __sub__(self, other):
        """
        Calculates the difference between the lengths of two vectors.

        Args:
            other (Vector): The vector to subtract.

        Returns:
            float: The difference between the lengths of the two vectors.

        Raises:
            ValueError: If the other object is not a Vector or dimensions do not match.
        """
        self.validation(other)
        n2 = math.sqrt(sum(x ** 2 for x in other.components))
        n1 = math.sqrt(sum(x ** 2 for x in self.components))
        return n1 - n2

    def calc_length(self, obj):
        """
        Calculates the lengths of the current vector and the given vector.

        Args:
            obj (Vector): The vector to calculate the length for.

        Returns:
            list: A list containing the lengths of the current vector and the given vector.
        """
        return [
            math.sqrt(sum(x ** 2 for x in self.components)),
            math.sqrt(sum(x ** 2 for x in obj.components))
        ]

    def __lt__(self, other):
        """
        Compares the lengths of two vectors.

        Args:
            other (Vector): The vector to compare.

        Returns:
            bool: True if the length of the current vector is less than the other vector.

        Raises:
            ValueError: If the other object is not a Vector or dimensions do not match.
        """
        self.validation(other)
        res = self.calc_length(other)
        return res[0] < res[1]

    def __mul__(self, other):
        """
        Multiplies the lengths of two vectors.

        Args:
            other (Vector): The vector to multiply.

        Returns:
            float: The product of the lengths of the two vectors.

        Raises:
            ValueError: If the other object is not a Vector or dimensions do not match.
        """
        self.validation(other)
        res = self.calc_length(other)
        return res[0] * res[1]

    def __eq__(self, other):
        """
        Checks if the lengths of two vectors are equal.

        Args:
            other (Vector): The vector to compare.

        Returns:
            bool: True if the lengths of the two vectors are equal.

        Raises:
            ValueError: If the other object is not a Vector or dimensions do not match.
        """
        self.validation(other)
        res = self.calc_length(other)
        return res[0] == res[1]


# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)  # Output: Sum of vector lengths
print(v1 < v2)  # Output: True or False based on lengths
print(v1 == v2)  # Output: True or False based on lengths
print(v1 * v2)  # Output: Product of vector lengths
