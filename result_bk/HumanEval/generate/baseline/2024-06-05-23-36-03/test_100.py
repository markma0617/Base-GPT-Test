from code_100 import make_a_pile

import unittest

def test():
    class TestMakeAPile(unittest.TestCase):

        def test_make_a_pile_odd(self):
            self.assertEqual(make_a_pile(3), [3, 5, 7])

        def test_make_a_pile_even(self):
            self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    return TestMakeAPile
