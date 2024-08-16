from code_158 import find_max

import unittest

def test_find_max(self):
    self.assertEqual(find_max(["name", "of", "string"]), "string")
    self.assertEqual(find_max(["name", "enam", "game"]), "enam")
    self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.FunctionTestCase(test_find_max))
