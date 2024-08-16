from code_121 import solution

import unittest

def test():
    class TestSolution(unittest.TestCase):
        
        def test_example_1(self):
            self.assertEqual(solution([5, 8, 7, 1]), 12)
        
        def test_example_2(self):
            self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        
        def test_example_3(self):
            self.assertEqual(solution([30, 13, 24, 321]), 0)

    unittest.main(argv=[''], exit=False)

test()
