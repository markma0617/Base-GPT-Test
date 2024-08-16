from code_157 import right_angle_triangle

import unittest

def test():
    class TestRightAngleTriangle(unittest.TestCase):
        
        def test_right_angle_triangle(self):
            self.assertTrue(right_angle_triangle(3, 4, 5))
            self.assertFalse(right_angle_triangle(1, 2, 3))
            self.assertTrue(right_angle_triangle(6, 8, 10))
            self.assertFalse(right_angle_triangle(5, 12, 13))
            self.assertTrue(right_angle_triangle(9, 12, 15))

    return TestRightAngleTriangle('test_right_angle_triangle')
