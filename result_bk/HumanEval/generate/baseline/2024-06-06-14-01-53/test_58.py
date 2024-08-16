from code_58 import common

import unittest
from your_script import common

class TestCommon(unittest.TestCase):

    def test_common_case1(self):
        result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        self.assertEqual(result, [1, 5, 653])

    def test_common_case2(self):
        result = common([5, 3, 2, 8], [3, 2])
        self.assertEqual(result, [2, 3])

    def test_common_empty_lists(self):
        result = common([], [])
        self.assertEqual(result, [])

    def test_common_no_common_elements(self):
        result = common([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
