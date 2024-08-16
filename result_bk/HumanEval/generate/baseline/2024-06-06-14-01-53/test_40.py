from code_40 import triples_sum_to_zero

import unittest

def test():
    class TestTriplesSumToZero(unittest.TestCase):

        def test_case1(self):
            self.assertEqual(triples_sum_to_zero([1, 3, 5, 0]), False)

        def test_case2(self):
            self.assertEqual(triples_sum_to_zero([1, 3, -2, 1]), True)

        def test_case3(self):
            self.assertEqual(triples_sum_to_zero([1, 2, 3, 7]), False)

        def test_case4(self):
            self.assertEqual(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), True)

        def test_case5(self):
            self.assertEqual(triples_sum_to_zero([1]), False)

    return TestTriplesSumToZero
