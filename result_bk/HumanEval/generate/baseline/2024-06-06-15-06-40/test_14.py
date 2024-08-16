from code_14 import all_prefixes

import unittest
from typing import List


def all_prefixes(string: str) -> List[str]:
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result


class TestAllPrefixes(unittest.TestCase):

    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertEqual(all_prefixes('hello'), ['h', 'he', 'hel', 'hell', 'hello'])
        self.assertEqual(all_prefixes('testing'), ['t', 'te', 'tes', 'test', 'testi', 'testin', 'testing'])
        self.assertEqual(all_prefixes('12345'), ['1', '12', '123', '1234', '12345'])


if __name__ == '__main__':
    unittest.main()
