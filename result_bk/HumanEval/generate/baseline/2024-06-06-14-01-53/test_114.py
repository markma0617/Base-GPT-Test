from code_114 import minSubArraySum

import unittest

def test():
    class TestMinSubArraySum(unittest.TestCase):
        
        def test_example1(self):
            result = minSubArraySum([2, 3, 4, 1, 2, 4])
            self.assertEqual(result, 1)
        
        def test_example2(self):
            result = minSubArraySum([-1, -2, -3])
            self.assertEqual(result, -6)
        
        def test_all_negative(self):
            result = minSubArraySum([-5, -10, -2, -8])
            self.assertEqual(result, -25)
        
        def test_all_positive(self):
            result = minSubArraySum([5, 10, 2, 8])
            self.assertEqual(result, 0)
        
        def test_mixed(self):
            result = minSubArraySum([-5, 3, 2, -8, 10])
            self.assertEqual(result, -8)
    
    return TestMinSubArraySum
