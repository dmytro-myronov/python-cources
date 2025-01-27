import os

class DirectoryFileIterator:
    """
    An iterator that yields files in a given directory along with their sizes.

    Attributes:
        directory (str): The path to the directory to iterate through.
        files (iterator): An iterator over the files and directories in the given directory.
    """
    def __init__(self, directory):
        """
        Initialize the iterator with the specified directory.

        Args:
            directory (str): The path to the directory to iterate through.
        """
        self.directory = directory
        self.files = iter(os.listdir(directory))

    def __iter__(self):
        """
        Return the iterator object.

        Returns:
            DirectoryFileIterator: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next file in the directory along with its size.

        Returns:
            tuple: A tuple containing the file name and its size in bytes.

        Raises:
            StopIteration: When there are no more files to iterate over.
        """
        while True:
            try:
                file_name = next(self.files)
                file_path = os.path.join(self.directory, file_name)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    return file_name, file_size
            except StopIteration:
                raise StopIteration

# Usage of the iterator
if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ").strip()

    if os.path.isdir(directory_path):
        print("List of files in the directory:")
        for file_name, file_size in DirectoryFileIterator(directory_path):
            print(f"{file_name}: {file_size} bytes")
    else:
        print("The specified path is not a directory.")
