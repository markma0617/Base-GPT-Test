from code_15 import string_sequence

import unittest
from your_module import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_string_sequence_with_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_string_sequence_with_positive_number(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_string_sequence_with_negative_number(self):
        self.assertEqual(string_sequence(-3), '0 -1 -2 -3')

if __name__ == '__main__':
    unittest.main()
