from code_32 import find_zero
from code_32 import poly

import unittest
from your_module import poly, find_zero


class TestPolyFunction(unittest.TestCase):

    def test_poly_function(self):
        self.assertEqual(poly([1, 2], 0), 1)  # 1
        self.assertEqual(poly([1, 2], 1), 3)  # 1 + 2*1
        self.assertEqual(poly([1, 2, 3], 2), 17)  # 1 + 2*2 + 3*2^2
        self.assertAlmostEqual(poly([1, -2, 3, -4], 3), 34)  # 1 - 2*3 + 3*3^2 - 4*3^3


class TestFindZeroFunction(unittest.TestCase):

    def test_find_zero_function(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)  # f(x) = 1 + 2x
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3


if __name__ == '__main__':
    unittest.main()
