from code_163 import generate_integers

import unittest
from your_module import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_ascend_order(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_generate_integers_descend_order(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_generate_integers_no_even_digits(self):
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()
