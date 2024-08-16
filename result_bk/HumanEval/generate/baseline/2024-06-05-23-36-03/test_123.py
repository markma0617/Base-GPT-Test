from code_123 import get_odd_collatz

import unittest

def test():
    class TestGetOddCollatz(unittest.TestCase):
        def test_case1(self):
            self.assertEqual(get_odd_collatz(5), [1, 5])

        def test_case2(self):
            self.assertEqual(get_odd_collatz(7), [1, 3, 5, 7])

        def test_case3(self):
            self.assertEqual(get_odd_collatz(10), [1])

        def test_case4(self):
            self.assertEqual(get_odd_collatz(1), [1])

    return TestGetOddCollatz

