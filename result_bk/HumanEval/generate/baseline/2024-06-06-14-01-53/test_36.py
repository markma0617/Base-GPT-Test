from code_36 import fizz_buzz

import unittest
from your_module import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_50(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_78(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_79(self):
        self.assertEqual(fizz_buzz(79), 3)

if __name__ == '__main__':
    unittest.main()
