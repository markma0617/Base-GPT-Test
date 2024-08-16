from code_45 import triangle_area

import unittest

def test():
    class TestTriangleArea(unittest.TestCase):
        def test_triangle_area(self):
            self.assertEqual(triangle_area(5, 3), 7.5)
    
    return TestTriangleArea('test_triangle_area')
