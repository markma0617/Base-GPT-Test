from code_85 import add

import unittest

def test():
    class TestAddFunction(unittest.TestCase):
        def test_example(self):
            self.assertEqual(add([4, 2, 6, 7]), 2)
        
        def test_empty_list(self):
            self.assertEqual(add([]), 0)
        
        def test_all_odd_elements(self):
            self.assertEqual(add([1, 3, 5, 7]), 0)
        
        def test_all_even_elements(self):
            self.assertEqual(add([2, 4, 6, 8]), 0)
        
        def test_mixed_elements(self):
            self.assertEqual(add([4, 2, 6, 7, 10, 3]), 6)
    
    return TestAddFunction
