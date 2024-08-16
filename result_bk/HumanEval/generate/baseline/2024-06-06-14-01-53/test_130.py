from code_130 import tri

import unittest
from solution import tri

class TestTri(unittest.TestCase):

    def test_tri(self):
        self.assertEqual(tri(0), [1])
        self.assertEqual(tri(1), [1, 3])
        self.assertEqual(tri(2), [1, 3, 2])
        self.assertEqual(tri(3), [1, 3, 2, 8])
        self.assertEqual(tri(4), [1, 3, 2, 8, 3])
        self.assertEqual(tri(5), [1, 3, 2, 8, 3, 12])
        self.assertEqual(tri(6), [1, 3, 2, 8, 3, 12, 4])

if __name__ == '__main__':
    unittest.main()
