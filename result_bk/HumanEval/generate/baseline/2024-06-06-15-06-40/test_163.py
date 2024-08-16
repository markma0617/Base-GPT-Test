from code_163 import generate_integers

import unittest
from your_module import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_example1(self):
        result = generate_integers(2, 8)
        self.assertEqual(result, [2, 4, 6, 8])

    def test_generate_integers_example2(self):
        result = generate_integers(8, 2)
        self.assertEqual(result, [2, 4, 6, 8])

    def test_generate_integers_example3(self):
        result = generate_integers(10, 14)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
