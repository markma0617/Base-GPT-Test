from code_71 import triangle_area

import unittest

def test():
    class TestTriangleArea(unittest.TestCase):
        
        def test_valid_triangle(self):
            self.assertEqual(triangle_area(3, 4, 5), 6.00)
        
        def test_invalid_triangle(self):
            self.assertEqual(triangle_area(1, 2, 10), -1)
            
    return TestTriangleArea
