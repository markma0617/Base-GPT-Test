from code_127 import intersection

import unittest

def test():
    class TestIntersection(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(intersection((1, 2), (2, 3)), "NO")

        def test_example_2(self):
            self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

        def test_example_3(self):
            self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    return TestIntersection
