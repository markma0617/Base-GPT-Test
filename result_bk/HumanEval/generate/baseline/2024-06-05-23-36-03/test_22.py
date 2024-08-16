from code_22 import filter_integers

import unittest
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]


class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers_only_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_filter_integers_mixed_values(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
