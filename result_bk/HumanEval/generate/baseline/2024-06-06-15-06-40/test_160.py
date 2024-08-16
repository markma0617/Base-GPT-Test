from code_160 import do_algebra

import unittest

def test():
    class TestDoAlgebra(unittest.TestCase):

        def test_example_case(self):
            operator = ['+', '*', '-']
            operand = [2, 3, 4, 5]
            self.assertEqual(do_algebra(operator, operand), 9)

        def test_single_operator(self):
            operator = ['*']
            operand = [2, 3, 4]
            self.assertEqual(do_algebra(operator, operand), 8)

        def test_multiple_operators(self):
            operator = ['+', '-', '*', '/']
            operand = [4, 2, 3, 5, 6]
            self.assertEqual(do_algebra(operator, operand), 2)

        def test_large_numbers(self):
            operator = ['+', '*']
            operand = [9999, 9999, 9999]
            self.assertEqual(do_algebra(operator, operand), 99980001)

        def test_division(self):
            operator = ['//']
            operand = [10, 2]
            self.assertEqual(do_algebra(operator, operand), 5)

    return TestDoAlgebra
