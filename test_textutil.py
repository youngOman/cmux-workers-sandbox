import unittest

from textutil import slugify


class SlugifyTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_lowercase_and_spaces(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_consecutive_symbols(self):
        self.assertEqual(slugify("a!!--@@b  c"), "a-b-c")

    def test_leading_and_trailing_symbols(self):
        self.assertEqual(slugify("--Hello, World!--"), "hello-world")

    def test_only_symbols(self):
        self.assertEqual(slugify("!@#"), "")


if __name__ == "__main__":
    unittest.main()
