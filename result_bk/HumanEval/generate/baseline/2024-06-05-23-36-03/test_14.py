from code_14 import all_prefixes

import unittest
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result

class TestAllPrefixes(unittest.TestCase):

    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()
