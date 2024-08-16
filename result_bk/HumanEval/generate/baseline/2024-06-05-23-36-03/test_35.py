from code_35 import max_element

import unittest

def test():
    class TestMaxElement(unittest.TestCase):
        
        def test_max_element(self):
            self.assertEqual(max_element([1, 2, 3]), 3)
            self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
    
    return TestMaxElement
