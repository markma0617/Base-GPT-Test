from code_152 import compare

import unittest
from <your_module_name> import compare

class TestCompareFunction(unittest.TestCase):

    def test_correct_guesses(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])

    def test_incorrect_guesses(self):
        self.assertEqual(compare([1,2,3,4,5,1],[0,0,0,0,0,0]), [1,2,3,4,5,1])
        self.assertEqual(compare([1,2,3,4,5,1],[2,2,2,2,2,2]), [1,0,1,2,3,1])

    def test_mixed_guesses(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,2,2,2,1]), [0,0,1,2,3,0])
        self.assertEqual(compare([1,2,3,4,5,1],[0,3,4,1,5,0]), [1,1,1,3,0,1])

if __name__ == '__main__':
    unittest.main()
