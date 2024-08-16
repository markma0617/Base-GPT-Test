from code_114 import minSubArraySum

import unittest

def test():
    class TestMinSubArraySum(unittest.TestCase):
        
        def test_example1(self):
            self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        
        def test_example2(self):
            self.assertEqual(minSubArraySum([-1, -2, -3]), -6)
    
    unittest.main(argv=[''], exit=False)

test()
