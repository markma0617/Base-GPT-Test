from code_144 import simplify

import unittest
from your_module import simplify

class TestSimplifyFunction(unittest.TestCase):

    def test_simplify_whole_number(self):
        self.assertTrue(simplify("1/5", "5/1"))

    def test_simplify_not_whole_number(self):
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))

if __name__ == '__main__':
    unittest.main()
