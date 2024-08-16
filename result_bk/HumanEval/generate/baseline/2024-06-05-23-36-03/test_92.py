from code_92 import any_int

import unittest

def test():
    class TestAnyInt(unittest.TestCase):

        def test_valid_numbers(self):
            self.assertTrue(any_int(5, 2, 7))
            self.assertTrue(any_int(3, -2, 1))

        def test_invalid_numbers(self):
            self.assertFalse(any_int(3, 2, 2))
            self.assertFalse(any_int(3.6, -2.2, 2))

    return TestAnyInt
