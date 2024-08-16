from code_49 import modp

import unittest

def test():
    class TestModP(unittest.TestCase):

        def test_modp(self):
            self.assertEqual(modp(3, 5), 3)
            self.assertEqual(modp(1101, 101), 2)
            self.assertEqual(modp(0, 101), 1)
            self.assertEqual(modp(3, 11), 8)
            self.assertEqual(modp(100, 101), 1)

    return TestModP('test_modp')
