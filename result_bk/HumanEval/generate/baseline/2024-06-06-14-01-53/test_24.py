from code_24 import largest_divisor
import unittest

def test():
    class TestLargestDivisor(unittest.TestCase):
        def test_largest_divisor(self):
            self.assertEqual(largest_divisor(15), 5)

    unittest.main(argv=[''], exit=False)