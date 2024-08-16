from code_29 import filter_by_prefix

import unittest
from your_module import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_multiple_elements_with_prefix(self):
        input_list = ['abc', 'bcd', 'cde', 'array']
        self.assertEqual(filter_by_prefix(input_list, 'a'), ['abc', 'array'])

    def test_no_elements_with_prefix(self):
        input_list = ['bcd', 'cde']
        self.assertEqual(filter_by_prefix(input_list, 'a'), [])

if __name__ == '__main__':
    unittest.main()
