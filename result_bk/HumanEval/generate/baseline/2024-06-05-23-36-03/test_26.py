from code_26 import remove_duplicates

import unittest
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_remove_duplicates_empty(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [])
        
    def test_remove_duplicates_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
