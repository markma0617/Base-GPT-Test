from code_151 import double_the_difference

import unittest

def double_the_difference(lst):
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

class TestDoubleTheDifference(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([9, 0]), 81)

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(double_the_difference([1, -2, 3, -4, 5]), 35)

if __name__ == '__main__':
    unittest.main()
