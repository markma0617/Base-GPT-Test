from code_146 import specialFilter

import unittest

def test_specialFilter(self):
    self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
    self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
    self.assertEqual(specialFilter([-3, -5, -7, 15]), 1)
    self.assertEqual(specialFilter([11, 99, 101, 22, 33, 44]), 1)
    self.assertEqual(specialFilter([]), 0)

class TestSpecialFilter(unittest.TestCase):
    test_specialFilter = test_specialFilter

if __name__ == '__main__':
    unittest.main()
