from code_159 import eat

import unittest
from your_module import eat

class TestEat(unittest.TestCase):

    def test_1(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_2(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_3(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_4(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()
