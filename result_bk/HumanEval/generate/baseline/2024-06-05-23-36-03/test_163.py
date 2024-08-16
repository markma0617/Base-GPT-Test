from code_163 import generate_integers

import unittest
from your_module import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(5, 5), [4, 6, 8])

if __name__ == '__main__':
    unittest.main()
