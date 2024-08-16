from code_32 import poly

import unittest
from your_module import poly, find_zero


class TestPolynomial(unittest.TestCase):

    def test_poly(self):
        self.assertAlmostEqual(poly([1, 2], 2), 5)  # f(x) = 1 + 2x
        self.assertAlmostEqual(poly([-6, 11, -6, 1], 1), 0)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3

    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5)  # f(x) = 1 + 2x
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3


if __name__ == '__main__':
    unittest.main()
