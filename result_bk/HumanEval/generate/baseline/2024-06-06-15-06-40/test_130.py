from code_130 import tri

import unittest
from your_file import tri

class TestTribonacci(unittest.TestCase):

    def test_tribonacci(self):
        self.assertEqual(tri(0), [1])
        self.assertEqual(tri(1), [1, 3])
        self.assertEqual(tri(2), [1, 3, 2])
        self.assertEqual(tri(3), [1, 3, 2, 8])
        self.assertEqual(tri(4), [1, 3, 2, 8, 4])
        # Add more test cases if needed

if __name__ == '__main__':
    unittest.main()
