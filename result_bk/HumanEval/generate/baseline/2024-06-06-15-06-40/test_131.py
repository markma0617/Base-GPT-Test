from code_131 import digits

import unittest
from function_to_test import digits

class TestDigits(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(digits(1), 1)

    def test_example_2(self):
        self.assertEqual(digits(4), 0)

    def test_example_3(self):
        self.assertEqual(digits(235), 15)

if __name__ == '__main__':
    unittest.main()
