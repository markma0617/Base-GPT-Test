from code_63 import fibfib

import unittest

def test():
    class TestFibFib(unittest.TestCase):
        
        def test_fibfib(self):
            self.assertEqual(fibfib(1), 0)
            self.assertEqual(fibfib(5), 4)
            self.assertEqual(fibfib(8), 24)
            self.assertEqual(fibfib(10), 96)  # Add more test cases as needed

    return TestFibFib
