from code_32 import find_zero
from code_32 import poly

import math
import unittest
from your_module import poly, find_zero

class TestPolynomial(unittest.TestCase):

    def test_poly(self):
        self.assertAlmostEqual(poly([1, 2], 2), 5)
        self.assertAlmostEqual(poly([2, 3, 4], 3), 47)

    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5)
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0)

if __name__ == '__main__':
    unittest.main()
