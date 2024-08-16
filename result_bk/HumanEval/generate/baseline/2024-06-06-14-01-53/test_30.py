from code_30 import get_positive

import unittest

def test():
    class TestGetPositive(unittest.TestCase):
        
        def test_1(self):
            self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        
        def test_2(self):
            self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
    
    return TestGetPositive
