from code_119 import check
from code_119 import match_parens

import unittest

def test():
    class TestMatchParens(unittest.TestCase):

        def test_good_string_possible(self):
            self.assertEqual(match_parens(['()(', ')']), 'Yes')
            self.assertEqual(match_parens(['()', ')']), 'Yes')
            self.assertEqual(match_parens(['(', ')']), 'Yes')
            self.assertEqual(match_parens(['))', '()']), 'Yes')
            self.assertEqual(match_parens(['(', '()']), 'Yes')

        def test_no_good_string_possible(self):
            self.assertEqual(match_parens([')', ')']), 'No')
            self.assertEqual(match_parens(['(', '(']), 'No')
            self.assertEqual(match_parens(['))', '))']), 'No')
            self.assertEqual(match_parens(['()', '())']), 'No')
            self.assertEqual(match_parens(['(()', '())']), 'No')

    return TestMatchParens
