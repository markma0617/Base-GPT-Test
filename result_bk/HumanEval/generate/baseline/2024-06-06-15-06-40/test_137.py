from code_137 import compare_one

import unittest

def test():
    class TestCompareOne(unittest.TestCase):
        
        def test_integers(self):
            self.assertEqual(compare_one(1, 2), 2)
            self.assertIsNone(compare_one(1, 1))

        def test_floats(self):
            self.assertEqual(compare_one(1.5, 2.5), 2.5)
            self.assertIsNone(compare_one(1.0, 1.0))

        def test_mixed_types(self):
            self.assertEqual(compare_one(1, "2,3"), "2,3")
            self.assertEqual(compare_one("5,1", "6"), "6")
            self.assertIsNone(compare_one("1", 1))

    return TestCompareOne
