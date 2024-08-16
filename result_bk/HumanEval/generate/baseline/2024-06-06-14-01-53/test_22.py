from code_22 import filter_integers

import unittest
from my_module import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers_with_integers_and_non_integers(self):
        values = ['a', 3.14, 5]
        result = filter_integers(values)
        self.assertEqual(result, [5])

    def test_filter_integers_with_integers_and_other_types(self):
        values = [1, 2, 3, 'abc', {}, []]
        result = filter_integers(values)
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
