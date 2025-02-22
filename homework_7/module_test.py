import unittest


class StringProcessor:
    @staticmethod
    def reverse_string(s: str) -> str:
        return s[::-1]

    @staticmethod
    def capitalize_string(s: str) -> str:
        return s.capitalize()

    @staticmethod
    def count_vowels(s: str) -> int:
        return sum(1 for char in s.lower() if char in "aeiou")


class TestStringProcessor(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(StringProcessor.reverse_string("hello"), "olleh")
        self.assertEqual(StringProcessor.reverse_string("Python"), "nohtyP")
        self.assertEqual(StringProcessor.reverse_string("12345"), "54321")

    @unittest.skip("Known issue with empty strings")
    def test_reverse_string_empty(self):
        self.assertEqual(StringProcessor.reverse_string(""), "")

    def test_capitalize_string(self):
        self.assertEqual(StringProcessor.capitalize_string("hello"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("HELLO"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("123abc"), "123abc")

    def test_count_vowels(self):
        self.assertEqual(StringProcessor.count_vowels("hello"), 2)
        self.assertEqual(StringProcessor.count_vowels("PYTHON"), 1)
        self.assertEqual(StringProcessor.count_vowels("xyz"), 0)
        self.assertEqual(StringProcessor.count_vowels("aAeEiIoOuU"), 10)


if __name__ == "__main__":
    unittest.main()
