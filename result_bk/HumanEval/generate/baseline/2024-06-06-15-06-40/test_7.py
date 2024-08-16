from code_7 import filter_by_substring

import unittest
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_strings_with_substring(self):
        input_strings = ['abc', 'bacd', 'cde', 'array']
        expected_output = ['abc', 'bacd', 'array']
        self.assertEqual(filter_by_substring(input_strings, 'a'), expected_output)


if __name__ == '__main__':
    unittest.main()
