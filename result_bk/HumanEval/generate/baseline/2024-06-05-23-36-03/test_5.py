from code_5 import intersperse

import unittest

from my_module import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_intersperse_numbers(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()
