from code_160 import do_algebra

import unittest

def test():
    class TestDoAlgebra(unittest.TestCase):

        def test_addition(self):
            operator = ['+']
            operand = [2, 3, 4]
            self.assertEqual(do_algebra(operator, operand), 9)

        def test_subtraction(self):
            operator = ['-']
            operand = [7, 3, 2]
            self.assertEqual(do_algebra(operator, operand), 2)

        def test_multiplication(self):
            operator = ['*']
            operand = [2, 3, 4]
            self.assertEqual(do_algebra(operator, operand), 14)

        def test_floor_division(self):
            operator = ['//']
            operand = [10, 2, 3]
            self.assertEqual(do_algebra(operator, operand), 4)

        def test_exponentiation(self):
            operator = ['**']
            operand = [2, 3, 2]
            self.assertEqual(do_algebra(operator, operand), 64)

    return TestDoAlgebra
