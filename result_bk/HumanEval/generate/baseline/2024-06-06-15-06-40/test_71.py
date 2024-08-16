from code_71 import triangle_area

import unittest
from your_module import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        
    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)
        
    def test_equilateral_triangle(self):
        self.assertEqual(triangle_area(4, 4, 4), 6.93)
        
    def test_isosceles_triangle(self):
        self.assertEqual(triangle_area(3, 3, 4), 4.47)
        
    def test_right_angled_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        
    def test_large_triangle(self):
        self.assertEqual(triangle_area(1000, 20, 1000), 9999.50)

if __name__ == '__main__':
    unittest.main()
