from code_62 import derivative

import unittest

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]

class TestDerivative(unittest.TestCase):

    def test_derivative_1(self):
        result = derivative([3, 1, 2, 4, 5])
        self.assertEqual(result, [1, 4, 12, 20])

    def test_derivative_2(self):
        result = derivative([1, 2, 3])
        self.assertEqual(result, [2, 6])

if __name__ == '__main__':
    unittest.main()
