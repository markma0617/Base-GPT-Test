from code_104 import unique_digits

import unittest
from your_module import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits_example1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_unique_digits_example2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_unique_digits_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_unique_digits_single_element(self):
        self.assertEqual(unique_digits([375]), [375])

    def test_unique_digits_all_even_digits(self):
        self.assertEqual(unique_digits([222, 444, 666]), [])

    def test_unique_digits_all_odd_digits(self):
        self.assertEqual(unique_digits([135, 975, 753]), [135, 753, 975])

if __name__ == '__main__':
    unittest.main()
