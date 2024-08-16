from code_105 import by_length

import unittest

def test():
    class TestByLength(unittest.TestCase):
        def test_example1(self):
            arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            self.assertEqual(by_length(arr), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])

        def test_empty_array(self):
            arr = []
            self.assertEqual(by_length(arr), [])

        def test_strange_number(self):
            arr = [1, -1, 55]
            self.assertEqual(by_length(arr), ['One'])
    
    return TestByLength
