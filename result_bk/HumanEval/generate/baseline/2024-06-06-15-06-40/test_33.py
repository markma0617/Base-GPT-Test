from code_33 import sort_third

import unittest

def test():
    class TestSortThird(unittest.TestCase):
        
        def test_example1(self):
            self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        
        def test_example2(self):
            self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    return TestSortThird
