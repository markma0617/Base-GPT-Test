from code_28 import concatenate

import unittest
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

class TestConcatenate(unittest.TestCase):

    def test_concatenate_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenate_list_of_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()
