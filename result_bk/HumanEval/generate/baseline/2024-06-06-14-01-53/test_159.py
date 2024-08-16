from code_159 import eat

import unittest
from your_module import eat

class TestEatFunction(unittest.TestCase):

    def test_eat_enough_carrots(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_eat_not_enough_carrots(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_eat_zero_carrots(self):
        self.assertEqual(eat(0, 0, 0), [0, 0])

    def test_eat_all_remaining_carrots(self):
        self.assertEqual(eat(5, 7, 5), [10, 0])

if __name__ == '__main__':
    unittest.main()
