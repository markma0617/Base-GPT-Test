from code_128 import prod_signs

import unittest

def test_prod_signs():
    class TestProdSigns(unittest.TestCase):
        def test_example1(self):
            self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

        def test_example2(self):
            self.assertEqual(prod_signs([0, 1]), 0)

        def test_empty_arr(self):
            self.assertIsNone(prod_signs([]))

    return TestProdSigns

if __name__ == '__main__':
    unittest.main()
