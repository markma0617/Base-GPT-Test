from code_47 import median

import unittest

def test():
    class TestMedian(unittest.TestCase):
        
        def test_odd_list(self):
            self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        
        def test_even_list(self):
            self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
    
    return TestMedian
