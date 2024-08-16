from code_107 import even_odd_palindrome

import unittest
from even_odd_palindrome import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
    
    def test_example2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_boundary_case(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))
    
    def test_large_case(self):
        self.assertEqual(even_odd_palindrome(1000), (38, 58))

if __name__ == '__main__':
    unittest.main()
