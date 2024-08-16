from code_29 import filter_by_prefix

import unittest
from my_module import filter_by_prefix


class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_nonempty_list(self):
        input_list = ['abc', 'bcd', 'cde', 'array']
        self.assertEqual(filter_by_prefix(input_list, 'a'), ['abc', 'array'])


if __name__ == '__main__':
    unittest.main()
