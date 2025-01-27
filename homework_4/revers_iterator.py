
from jedi.inference.value.iterable import Generator


class ReverseIterator:


        def read_file(self, filename: str)-> Generator:
            """
            Reads a file and yields its lines in reverse order.

            This method opens the specified file, reads all lines, and then yields
            the lines one by one in reverse order after stripping any surrounding
            whitespace. It ensures the file is properly closed after the operation.

            :param filename: The name of the file to be read.
            :type filename: str
            :return: A generator that yields lines of the file in reverse order with
                surrounding whitespace removed.
            :rtype: Generator
            """
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines[::-1]:
                    # first_line = file.readline().strip()
                    yield line.strip()


iterator_reverse = ReverseIterator()
gen = iterator_reverse.read_file('filename.txt')

for text in gen:
    print(text)
