class Average:
    """
    A class to read numeric values from a file and compute their average.
    """

    def _read_file(self, filename: str):
        """
        Reads a file line by line and yields each line after stripping whitespace.

        :param filename: The name of the file to read.
        :yield: Stripped lines from the file.
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print("File not found. Enter correct filename")
            exit(1)

    def find_avg(self, filename: str):
        """
        Computes the average of numeric values read from a file.

        :param filename: The name of the file containing numeric values.
        :return: The average of numeric values in the file.
        """
        num_list = []
        i = 0
        for num in self._read_file(filename):
            try:
                num_list.append(float(num))
            except ValueError:
                print(f"Found non-numeric value. Skipping line {i}")
            i += 1

        if len(num_list) <= 1:
            print("No numeric values found or only one numeric value found. Cannot calculate average.")
            exit(1)

        return sum(num_list) / len(num_list)


if __name__ == "__main__":
    avg = Average()
    filename = input("Please enter filename: ")
    print(avg.find_avg(filename))
