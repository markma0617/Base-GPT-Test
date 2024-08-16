from code_146 import specialFilter

import unittest
from your_module import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_specialFilter_example1(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_specialFilter_example2(self):
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_specialFilter_all_elements_special(self):
        self.assertEqual(specialFilter([13, -33, 15, -37]), 4)

    def test_specialFilter_no_special_elements(self):
        self.assertEqual(specialFilter([22, 44, 68, 10, 9]), 0)

if __name__ == '__main__':
    unittest.main()
