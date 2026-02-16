import unittest

from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_get_title(self):
        md = '# Hello'
        result = extract_title(md)
        self.assertEqual('Hello', result)

    def test_get_title(self):
        md = 'Hello'
        with self.assertRaises(Exception):
            result = extract_title(md)

