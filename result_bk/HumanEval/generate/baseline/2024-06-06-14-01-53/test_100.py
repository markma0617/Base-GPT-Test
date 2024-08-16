from code_100 import make_a_pile

import unittest

def make_a_pile(n):
    return [n + 2*i for i in range(n)]

class TestMakeAPile(unittest.TestCase):

    def test_make_a_pile_odd_n(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

    def test_make_a_pile_even_n(self):
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_make_a_pile_single_level(self):
        self.assertEqual(make_a_pile(1), [1])

    def test_make_a_pile_zero_n(self):
        self.assertEqual(make_a_pile(0), [])

if __name__ == '__main__':
    unittest.main()
