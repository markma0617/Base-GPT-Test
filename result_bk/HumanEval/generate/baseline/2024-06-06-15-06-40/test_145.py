from code_145 import order_by_points

import unittest

def test_order_by_points():
    class TestOrderByPoints(unittest.TestCase):
        
        def test_order_by_points_example1(self):
            self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])

        def test_order_by_points_example2(self):
            self.assertEqual(order_by_points([]), [])

    return TestOrderByPoints

