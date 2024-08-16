from code_152 import compare

import unittest
from my_module import compare

class TestCompareFunction(unittest.TestCase):

    def test_compare_correct_guesses(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected = [0, 0, 0, 0, 0, 3]
        self.assertEqual(compare(game, guess), expected)

    def test_compare_incorrect_guesses(self):
        game = [0, 5, 0, 0, 0, 4]
        guess = [4, 1, 1, 0, 0, -2]
        expected = [4, 4, 1, 0, 0, 6]
        self.assertEqual(compare(game, guess), expected)

if __name__ == '__main__':
    unittest.main()
