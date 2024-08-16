from code_84 import solve

import unittest

def test():
    class TestSolve(unittest.TestCase):
        
        def test_case1(self):
            self.assertEqual(solve(1000), "1")
        
        def test_case2(self):
            self.assertEqual(solve(150), "110")
        
        def test_case3(self):
            self.assertEqual(solve(147), "1100")
        
        def test_case4(self):
            self.assertEqual(solve(0), "0")
        
        def test_case5(self):
            self.assertEqual(solve(8888), "101")
    
    unittest.main(argv=[''], exit=False)

test()
