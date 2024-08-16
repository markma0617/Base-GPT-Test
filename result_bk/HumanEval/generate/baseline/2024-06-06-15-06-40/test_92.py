from code_92 import any_int

import unittest
from your_module import any_int

class TestAnyInt(unittest.TestCase):

    def test_true_case(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))
        
    def test_false_case(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3.6, -2.2, 2))
        
    def test_invalid_inputs(self):
        self.assertFalse(any_int(3.6, 2, 1))
        self.assertFalse(any_int('a', 2, 1))
        self.assertFalse(any_int(3, 'b', 1))

if __name__ == '__main__':
    unittest.main()
