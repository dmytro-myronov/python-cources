import pytest
from file_processor import FileProcessor

@pytest.fixture
def processor():
    return FileProcessor()

def test_write_and_read(tmpdir, processor):
    # Створюємо тимчасовий файл у tmpdir
    temp_file = tmpdir.join("testfile.txt")

    data = "Hello, pytest!"
    # Записуємо дані у файл
    processor.write_to_file(str(temp_file), data)

    # Читаємо дані з файлу
    content = processor.read_from_file(str(temp_file))

    assert content == data

def test_write_overwrites_file(tmpdir, processor):
    temp_file = tmpdir.join("testfile.txt")

    processor.write_to_file(str(temp_file), "First line")
    processor.write_to_file(str(temp_file), "Second line")

    content = processor.read_from_file(str(temp_file))
    assert content == "Second line"

def test_read_empty_file(tmpdir, processor):
    temp_file = tmpdir.join("emptyfile.txt")
    # Створюємо порожній файл
    temp_file.write("")

    content = processor.read_from_file(str(temp_file))
    assert content == ""
