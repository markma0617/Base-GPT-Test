from code_130 import tri

import unittest
from your_module import tri

class TestTri(unittest.TestCase):

    def test_tri_with_n_equals_0(self):
        self.assertEqual(tri(0), [1])

    def test_tri_with_n_equals_3(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])

    def test_tri_with_n_equals_5(self):
        self.assertEqual(tri(5), [1, 3, 2, 8, 4, 17])

    def test_tri_with_n_equals_8(self):
        self.assertEqual(tri(8), [1, 3, 2, 8, 4, 17, 6, 27, 10, 37])

if __name__ == '__main__':
    unittest.main()
