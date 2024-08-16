from code_45 import triangle_area

import unittest

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2.0

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()
