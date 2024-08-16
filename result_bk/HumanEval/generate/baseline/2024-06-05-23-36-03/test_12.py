from code_12 import longest

import unittest
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_character_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_different_length_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()
