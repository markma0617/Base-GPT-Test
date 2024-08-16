from code_137 import compare_one

import unittest

def test():
    
    class TestCompareOne(unittest.TestCase):

        def test_integers(self):
            self.assertEqual(compare_one(1, 2), 2)

        def test_floats(self):
            self.assertEqual(compare_one(1.5, 3.2), 3.2)

        def test_strings_with_commas(self):
            self.assertEqual(compare_one("2,4", "3.5"), "3.5")

        def test_mixed_types_same_values(self):
            self.assertIsNone(compare_one("3.0", 3))

        def test_mixed_types_different_values(self):
            self.assertEqual(compare_one("1.2", 1.1), 1.2)

    return TestCompareOne
