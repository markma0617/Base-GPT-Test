from code_104 import unique_digits

import unittest
from test_module import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits_1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_unique_digits_2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_unique_digits_empty(self):
        self.assertEqual(unique_digits([]), [])

    def test_unique_digits_single_element(self):
        self.assertEqual(unique_digits([7]), [7])

if __name__ == '__main__':
    unittest.main()
