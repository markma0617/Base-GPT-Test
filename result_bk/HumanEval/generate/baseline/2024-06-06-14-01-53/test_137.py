from code_137 import compare_one

import unittest

def test():
    class TestCompareOne(unittest.TestCase):
        
        def test_integers(self):
            self.assertEqual(compare_one(1, 2), 2)
            self.assertEqual(compare_one(5, 5), None)
        
        def test_floats(self):
            self.assertEqual(compare_one(1.5, 2.5), 2.5)
            self.assertEqual(compare_one(3.0, "2.0"), "2.0")
        
        def test_mixed_types(self):
            self.assertEqual(compare_one("5.1", "6"), "6")
            self.assertEqual(compare_one("1", 1), None)
        
        def test_strings_with_comma(self):
            self.assertEqual(compare_one("1,5", "2.0"), 2.0)
            self.assertEqual(compare_one("5,1", "5.1"), "5.1")
    
    return TestCompareOne
