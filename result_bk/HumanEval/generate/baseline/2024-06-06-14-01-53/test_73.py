from code_73 import smallest_change

import unittest

def test():
    class TestSmallestChange(unittest.TestCase):
        
        def test_example1(self):
            arr = [1, 2, 3, 5, 4, 7, 9, 6]
            self.assertEqual(smallest_change(arr), 4)

        def test_example2(self):
            arr = [1, 2, 3, 4, 3, 2, 2]
            self.assertEqual(smallest_change(arr), 1)

        def test_example3(self):
            arr = [1, 2, 3, 2, 1]
            self.assertEqual(smallest_change(arr), 0)

    return TestSmallestChange
