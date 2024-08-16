from code_127 import intersection

import unittest
from your_file import intersection

class TestIntersection(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_case2(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_case3(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()
