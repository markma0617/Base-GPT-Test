from code_12 import longest

import unittest
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_char_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_different_length_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')


if __name__ == '__main__':
    unittest.main()
