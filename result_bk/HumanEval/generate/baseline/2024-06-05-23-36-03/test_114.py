from code_114 import minSubArraySum

import unittest
from solution import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_minSubArraySum_example1(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_minSubArraySum_example2(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_minSubArraySum_cornerCase1(self):
        self.assertEqual(minSubArraySum([1, 2, 3]), -6)  # Expected result is -6

    def test_minSubArraySum_cornerCase2(self):
        self.assertEqual(minSubArraySum([-3, -2, -1]), -6)  # Expected result is -6

if __name__ == '__main__':
    unittest.main()
