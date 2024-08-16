from code_104 import unique_digits

import unittest
from your_module import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits_with_odd_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_unique_digits_with_even_digits(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_unique_digits_with_all_even_digits(self):
        self.assertEqual(unique_digits([2, 4, 6, 8]), [])

    def test_unique_digits_with_all_odd_digits(self):
        self.assertEqual(unique_digits([135, 357, 159]), [135, 159, 357])

    def test_unique_digits_with_mixed_digits(self):
        self.assertEqual(unique_digits([135, 246, 357]), [135, 357])

if __name__ == '__main__':
    unittest.main()
