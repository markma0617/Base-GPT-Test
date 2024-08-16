from code_157 import right_angle_triangle

import unittest

def test():
    class TestRightAngleTriangle(unittest.TestCase):
        
        def test_right_angle_triangle(self):
            self.assertEqual(right_angle_triangle(3, 4, 5), True)
            self.assertEqual(right_angle_triangle(1, 2, 3), False)
            # Add more test cases here
        
    return TestRightAngleTriangle('test_right_angle_triangle')

