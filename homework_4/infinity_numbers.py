import uuid


class UniqueInfinityGenerator:
    """
    A generator class that yields unique UUID values indefinitely until stopped.

    Methods:
        generate: Generates a unique UUID on each iteration. Stops when the value "stop" is sent to the generator.
    """

    def __init__(self):
        """
        Initializes the UniqueInfinityGenerator object.
        """
        pass

    def generate(self):
        """
        Yields a new unique UUID indefinitely until "stop" is received.

        Yields:
            uuid.UUID: A unique UUID value.

        Stops when the value "stop" is sent to the generator.
        """
        flag = True
        while flag:
            value = yield uuid.uuid4()
            if value == "stop":
                break


def add_line_to_file(lines):
    """
    Appends a list of lines to a file called 'infinity_number.txt'.

    Args:
        lines (list): A list of strings to be written to the file.
    """
    with open('infinity_number.txt', 'a') as file:
        for line in lines:
            file.write(str(line) + '\n')


# Initialize the generator
iterator_reverse = UniqueInfinityGenerator()

i = 0
list_el = []
while True:
    # Get the next UUID from the generator
    gen = iterator_reverse.generate()
    value = next(gen)
    list_el.append(value)

    # After generating 1000 UUIDs, stop the generator and write to file
    if i == 1000:
        try:
            gen.send("stop")
        except StopIteration as e:
            print("Stopping generator")
            add_line_to_file(list_el)  # Write the list of UUIDs to file
            pass

    i += 1
