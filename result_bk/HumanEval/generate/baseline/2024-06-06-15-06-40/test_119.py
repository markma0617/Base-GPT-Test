from code_119 import match_parens

import unittest

def test():
    class TestMatchParens(unittest.TestCase):
        def test_case1(self):
            self.assertEqual(match_parens(['()(', ')']), 'Yes')

        def test_case2(self):
            self.assertEqual(match_parens([')', ')']), 'No')

        def test_case3(self):
            self.assertEqual(match_parens(['(((', ')))']), 'Yes')

        def test_case4(self):
            self.assertEqual(match_parens(['(', ')']), 'Yes')

        def test_case5(self):
            self.assertEqual(match_parens(['()', ')']), 'Yes')

    return TestMatchParens
