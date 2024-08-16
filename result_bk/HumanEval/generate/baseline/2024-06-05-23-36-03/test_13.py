from code_13 import greatest_common_divisor

import unittest

def test():
    class TestGreatestCommonDivisor(unittest.TestCase):
        
        def test_gcd_1(self):
            self.assertEqual(greatest_common_divisor(3, 5), 1)
        
        def test_gcd_2(self):
            self.assertEqual(greatest_common_divisor(25, 15), 5)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGreatestCommonDivisor)
    unittest.TextTestRunner().run(suite)
