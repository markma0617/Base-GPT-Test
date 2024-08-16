from code_49 import modp

import unittest
from your_module import modp

class TestModP(unittest.TestCase):

    def test_modp_example1(self):
        self.assertEqual(modp(3, 5), 3)

    def test_modp_example2(self):
        self.assertEqual(modp(1101, 101), 2)

    def test_modp_example3(self):
        self.assertEqual(modp(0, 101), 1)

    def test_modp_example4(self):
        self.assertEqual(modp(3, 11), 8)

    def test_modp_example5(self):
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()
