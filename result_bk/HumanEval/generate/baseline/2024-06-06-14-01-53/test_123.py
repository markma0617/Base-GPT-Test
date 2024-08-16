from code_123 import get_odd_collatz

import unittest

def test():
    
    class TestGetOddCollatz(unittest.TestCase):
        
        def test_odd_collatz_5(self):
            self.assertEqual(get_odd_collatz(5), [1, 5])
        
        def test_odd_collatz_7(self):
            self.assertEqual(get_odd_collatz(7), [1, 7])
        
        def test_odd_collatz_10(self):
            self.assertEqual(get_odd_collatz(10), [1])
        
        def test_odd_collatz_20(self):
            self.assertEqual(get_odd_collatz(20), [1, 5])
        
        def test_odd_collatz_1(self):
            self.assertEqual(get_odd_collatz(1), [1])
            
    return TestGetOddCollatz
