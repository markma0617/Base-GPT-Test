from code_63 import fibfib

import unittest

def test():
    class TestFibFib(unittest.TestCase):
        
        def test_fibfib_0(self):
            self.assertEqual(fibfib(0), 0)
        
        def test_fibfib_1(self):
            self.assertEqual(fibfib(1), 0)
        
        def test_fibfib_2(self):
            self.assertEqual(fibfib(2), 1)
        
        def test_fibfib_5(self):
            self.assertEqual(fibfib(5), 4)
        
        def test_fibfib_8(self):
            self.assertEqual(fibfib(8), 24)
    
    return TestFibFib
