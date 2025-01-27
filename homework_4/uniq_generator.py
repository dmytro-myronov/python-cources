import uuid
from jedi.inference.value.iterable import Generator


class UniqueGenerator:
    """
    A class that generates unique UUID values up to a specified limit.

    Methods:
        generate: Generates a specified number of unique UUIDs.
    """

    def generate(self, limit: int) -> Generator:
        """
        Generates a specified number of unique UUID values.

        Args:
            limit (int): The number of UUIDs to generate.

        Yields:
            uuid.UUID: A unique UUID value for each iteration up to the specified limit.
        """
        for i in range(limit):
            yield uuid.uuid4()


# Example usage
iterator_reverse = UniqueGenerator()  # Initialize the generator
gen = iterator_reverse.generate(3)  # Generate 3 unique UUIDs

# Iterate over the generated UUIDs and print them
for un_id in gen:
    print(un_id)
