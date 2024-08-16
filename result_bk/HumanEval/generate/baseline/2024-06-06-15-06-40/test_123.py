from code_123 import get_odd_collatz

import unittest

def test_get_odd_collatz(self):
    self.assertEqual(get_odd_collatz(1), [1])
    self.assertEqual(get_odd_collatz(5), [1, 5])
    self.assertEqual(get_odd_collatz(10), [1])
    self.assertEqual(get_odd_collatz(15), [1, 3, 5, 9, 15])
    self.assertEqual(get_odd_collatz(20), [1, 3, 5])
    self.assertEqual(get_odd_collatz(25), [1, 3, 5, 13, 25])

# Add this test function to the test class
setattr(unittest.TestCase, 'test_get_odd_collatz', test_get_odd_collatz)
