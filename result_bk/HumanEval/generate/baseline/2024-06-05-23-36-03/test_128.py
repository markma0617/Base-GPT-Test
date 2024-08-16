from code_128 import prod_signs

import unittest

def test():
    class TestProdSigns(unittest.TestCase):
        def test_example_1(self):
            self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

        def test_example_2(self):
            self.assertEqual(prod_signs([0, 1]), 0)

        def test_empty_arr(self):
            self.assertIsNone(prod_signs([]))

    return TestProdSigns

