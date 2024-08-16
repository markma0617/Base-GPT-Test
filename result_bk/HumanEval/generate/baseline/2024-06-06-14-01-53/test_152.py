from code_152 import compare

import unittest
from your_module import compare

class TestCompareFunction(unittest.TestCase):

    def test_compare_correct_guesses(self):
        self.assertEqual(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]), [0, 0, 0, 0, 3, 3])
        self.assertEqual(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]), [4, 4, 1, 0, 0, 6])

    def test_compare_incorrect_guesses(self):
        self.assertEqual(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, 2]), [0, 0, 0, 0, 3, 1])
        self.assertEqual(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, 2]), [4, 4, 1, 0, 0, 2])

if __name__ == '__main__':
    unittest.main()
