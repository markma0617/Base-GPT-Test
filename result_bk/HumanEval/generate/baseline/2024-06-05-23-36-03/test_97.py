from code_97 import multiply

import unittest

def test():
    class TestMultiply(unittest.TestCase):

        def test_positive_numbers(self):
            self.assertEqual(multiply(148, 412), 16)
            self.assertEqual(multiply(19, 28), 72)
            self.assertEqual(multiply(2020, 1851), 0)

        def test_mixed_sign_numbers(self):
            self.assertEqual(multiply(14, -15), 20)
            self.assertEqual(multiply(-7, 6), 2)
            self.assertEqual(multiply(-3, -8), 24)
    
    return TestMultiply
