from code_6 import parse_nested_parens

import unittest
from your_module import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
        self.assertEqual(parse_nested_parens('() (((())))'), [1, 4])

if __name__ == '__main__':
    unittest.main()
