from code_107 import even_odd_palindrome

import unittest

def test_even_odd_palindrome():
    class TestEvenOddPalindrome(unittest.TestCase):

        def test_example1(self):
            self.assertEqual(even_odd_palindrome(3), (1, 2))

        def test_example2(self):
            self.assertEqual(even_odd_palindrome(12), (4, 6))

        def test_one_palindrome(self):
            self.assertEqual(even_odd_palindrome(1), (0, 1))

        def test_no_palindromes(self):
            self.assertEqual(even_odd_palindrome(10), (0, 0))

        def test_large_number(self):
            self.assertEqual(even_odd_palindrome(1000), (20, 40))

    return TestEvenOddPalindrome
