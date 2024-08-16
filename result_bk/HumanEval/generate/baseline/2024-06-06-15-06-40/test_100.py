from code_100 import make_a_pile

import unittest

def test():
    class TestMakeAPile(unittest.TestCase):

        def test_case1(self):
            self.assertEqual(make_a_pile(3), [3, 5, 7])

        def test_case2(self):
            self.assertEqual(make_a_pile(1), [1])

        def test_case3(self):
            self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    return TestMakeAPile
