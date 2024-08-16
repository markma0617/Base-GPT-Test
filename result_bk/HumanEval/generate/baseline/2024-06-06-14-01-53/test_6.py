from code_6 import parse_paren_group
from code_6 import parse_nested_parens

import unittest
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]


class TestParseNestedParens(unittest.TestCase):

    def test_parse_nested_parens(self):
        input_str = '(()()) ((())) () ((())()())'
        expected_output = [2, 3, 1, 3]
        self.assertEqual(parse_nested_parens(input_str), expected_output)

        input_str = '() (()) ()()'
        expected_output = [1, 2, 1]
        self.assertEqual(parse_nested_parens(input_str), expected_output)

        input_str = '()'
        expected_output = [1]
        self.assertEqual(parse_nested_parens(input_str), expected_output)


if __name__ == '__main__':
    unittest.main()
