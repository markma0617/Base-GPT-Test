from code_68 import pluck

import unittest

def test():
    class TestPluck(unittest.TestCase):

        def test_example1(self):
            self.assertEqual(pluck([4,2,3]), [2, 1])

        def test_example2(self):
            self.assertEqual(pluck([1,2,3]), [2, 1])

        def test_example3(self):
            self.assertEqual(pluck([]), [])

        def test_example4(self):
            self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    return TestPluck
