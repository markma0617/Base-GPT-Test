from code_73 import smallest_change

import unittest
from your_script import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_example1(self):
        result = smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
        self.assertEqual(result, 4)

    def test_example2(self):
        result = smallest_change([1, 2, 3, 4, 3, 2, 2])
        self.assertEqual(result, 1)

    def test_example3(self):
        result = smallest_change([1, 2, 3, 2, 1])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
