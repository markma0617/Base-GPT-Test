from code_111 import histogram

import unittest
from test_file import histogram

class TestHistogram(unittest.TestCase):

    def test_histogram_single_letter(self):
        self.assertEqual(histogram('a'), {'a': 1})

    def test_histogram_same_occurrence(self):
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})

    def test_histogram_multiple_letters(self):
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})

    def test_histogram_highest_occurrence(self):
        self.assertEqual(histogram('b b b b a'), {'b': 4})

    def test_histogram_empty_string(self):
        self.assertEqual(histogram(''), {})

if __name__ == '__main__':
    unittest.main()
