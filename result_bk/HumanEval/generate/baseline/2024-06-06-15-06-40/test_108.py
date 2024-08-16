from code_108 import count_nums

import unittest
from your_module import count_nums

class TestCountNums(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()
