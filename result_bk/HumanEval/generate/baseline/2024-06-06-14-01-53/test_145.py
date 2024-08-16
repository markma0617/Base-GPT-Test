from code_145 import digits_sum
from code_145 import order_by_points

import unittest

def test():
    class TestOrderByPoints(unittest.TestCase):
        
        def test_order_by_points(self):
            self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
            self.assertEqual(order_by_points([]), [])
            self.assertEqual(order_by_points([123, 5, 14, -99]), [-99, 5, 14, 123])

    return TestOrderByPoints
