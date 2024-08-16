from code_146 import specialFilter

import unittest
from your_module import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_specialFilter_case1(self):
        result = specialFilter([15, -73, 14, -15])
        self.assertEqual(result, 1)

    def test_specialFilter_case2(self):
        result = specialFilter([33, -2, -3, 45, 21, 109])
        self.assertEqual(result, 2)

    def test_specialFilter_case3(self):
        result = specialFilter([10, 20, 30, 40, 50])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
