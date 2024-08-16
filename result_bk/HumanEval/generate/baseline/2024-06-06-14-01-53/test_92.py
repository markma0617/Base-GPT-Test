from code_92 import any_int

import unittest

def test():
    class TestAnyInt(unittest.TestCase):
        
        def test_integer_sum_property(self):
            self.assertTrue(any_int(5, 2, 7))  # 5 + 2 = 7
            self.assertFalse(any_int(3, 2, 2))  # 3 + 2 != 2
            self.assertTrue(any_int(3, -2, 1))  # 3 + (-2) = 1
            self.assertFalse(any_int(3.6, -2.2, 2))  # Not all integers
        
        def test_non_integer_input(self):
            self.assertFalse(any_int(3.6, -2, 2))  # Mixed integers and floats
            self.assertFalse(any_int(3, 'hello', 2))  # Mixed integers and string
            self.assertFalse(any_int(5, 2, '7'))  # Mixed integers and string

    return TestAnyInt
