class BinaryNumber:
    def __init__(self, value):
        """
        Initializes a BinaryNumber instance with a binary string.

        Args:
            value (str): A string representing a binary number (only '0' and '1').

        Raises:
            ValueError: If the value contains characters other than '0' or '1'.
        """
        # Ensure the value is a binary string
        if not all(bit in '01' for bit in value):
            raise ValueError("Value must be a binary string.")
        self.value = value

    def __repr__(self):
        """
        Returns a string representation of the BinaryNumber instance.

        Returns:
            str: A string representation of the BinaryNumber.
        """
        return f"BinaryNumber('{self.value}')"

    def __and__(self, other):
        """
        Performs the bitwise AND operation between two BinaryNumber instances.

        Args:
            other (BinaryNumber): Another BinaryNumber instance to perform AND with.

        Returns:
            BinaryNumber: A new BinaryNumber instance resulting from the AND operation.

        Raises:
            TypeError: If the operand is not a BinaryNumber instance.
        """
        if not isinstance(other, BinaryNumber):
            raise TypeError("Operand must be of type BinaryNumber")

        # Pad both binary numbers to the same length
        length = max(len(self.value), len(other.value))
        self_padded = self.value.zfill(length)
        other_padded = other.value.zfill(length)

        # Perform the AND operation
        result = ''.join('1' if self_padded[i] == '1' and other_padded[i] == '1' else '0' for i in range(length))
        return BinaryNumber(result)

    def __or__(self, other):
        """
        Performs the bitwise OR operation between two BinaryNumber instances.

        Args:
            other (BinaryNumber): Another BinaryNumber instance to perform OR with.

        Returns:
            BinaryNumber: A new BinaryNumber instance resulting from the OR operation.

        Raises:
            TypeError: If the operand is not a BinaryNumber instance.
        """
        if not isinstance(other, BinaryNumber):
            raise TypeError("Operand must be of type BinaryNumber")

        # Pad both binary numbers to the same length
        length = max(len(self.value), len(other.value))
        self_padded = self.value.zfill(length)
        other_padded = other.value.zfill(length)

        # Perform the OR operation
        result = ''.join('1' if self_padded[i] == '1' or other_padded[i] == '1' else '0' for i in range(length))
        return BinaryNumber(result)

    def __xor__(self, other):
        """
        Performs the bitwise XOR operation between two BinaryNumber instances.

        Args:
            other (BinaryNumber): Another BinaryNumber instance to perform XOR with.

        Returns:
            BinaryNumber: A new BinaryNumber instance resulting from the XOR operation.

        Raises:
            TypeError: If the operand is not a BinaryNumber instance.
        """
        if not isinstance(other, BinaryNumber):
            raise TypeError("Operand must be of type BinaryNumber")

        # Pad both binary numbers to the same length
        length = max(len(self.value), len(other.value))
        self_padded = self.value.zfill(length)
        other_padded = other.value.zfill(length)

        # Perform the XOR operation
        result = ''.join('1' if self_padded[i] != other_padded[i] else '0' for i in range(length))
        return BinaryNumber(result)

    def __invert__(self):
        """
        Performs the bitwise NOT operation on the BinaryNumber instance.

        Returns:
            BinaryNumber: A new BinaryNumber instance resulting from the NOT operation.
        """
        # Invert all bits
        result = ''.join('1' if bit == '0' else '0' for bit in self.value)
        return BinaryNumber(result)


# Test the binary operations
def test_binary_operations():
    """
    Tests the bitwise operations (AND, OR, XOR, NOT) on BinaryNumber instances.
    """
    bin1 = BinaryNumber("1010")
    bin2 = BinaryNumber("1100")

    # AND operation
    assert (bin1 & bin2).value == "1000", "AND test failed"

    # OR operation
    assert (bin1 | bin2).value == "1110", "OR test failed"

    # XOR operation
    assert (bin1 ^ bin2).value == "0110", "XOR test failed"

    # NOT operation
    assert (~bin1).value == "0101", "NOT test failed"

    print("All tests passed!")


# Run the tests
test_binary_operations()
