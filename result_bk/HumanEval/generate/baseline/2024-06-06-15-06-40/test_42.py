from code_42 import incr_list

import unittest

def test():
    class TestIncrList(unittest.TestCase):
    
        def test_example1(self):
            self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
    
        def test_example2(self):
            self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
    
    return TestIncrList
