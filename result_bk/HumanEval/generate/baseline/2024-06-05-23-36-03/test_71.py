from code_71 import triangle_area

import unittest

def test_triangle_area(self):
    self.assertEqual(triangle_area(3, 4, 5), 6.00)
    self.assertEqual(triangle_area(1, 2, 10), -1)
    self.assertEqual(triangle_area(5, 12, 13), 30.0)
    self.assertEqual(triangle_area(8, 15, 17), 60.0)
    self.assertEqual(triangle_area(7, 24, 25), 84.0)
    self.assertEqual(triangle_area(9, 40, 41), 180.0)

class TestTriangleArea(unittest.TestCase):
    test_triangle_area = test_triangle_area

if __name__ == '__main__':
    unittest.main()
