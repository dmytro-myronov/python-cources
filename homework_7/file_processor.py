class FileProcessor:
    def write_to_file(self, file_path: str, data: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)

    def read_from_file(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
