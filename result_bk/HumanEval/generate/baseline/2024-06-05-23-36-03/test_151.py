from code_151 import double_the_difference

import unittest

def test():
    class TestDoubleTheDifference(unittest.TestCase):
        def test_example_cases(self):
            self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
            self.assertEqual(double_the_difference([-1, -2, 0]), 0)
            self.assertEqual(double_the_difference([9, -2]), 81)
            self.assertEqual(double_the_difference([0]), 0)
        
        def test_empty_list(self):
            self.assertEqual(double_the_difference([]), 0)
        
        def test_only_negative_numbers(self):
            self.assertEqual(double_the_difference([-3, -5, -1]), 0)
        
        def test_float_numbers(self):
            self.assertEqual(double_the_difference([2.5, 3.5]), 0)
        
        def test_mixed_numbers(self):
            self.assertEqual(double_the_difference([1, -2, 3.0, 5]), 26)
    
    return TestDoubleTheDifference
