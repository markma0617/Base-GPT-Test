from code_107 import is_palindrome
from code_107 import even_odd_palindrome

def test():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(10) == (3, 6)
    assert even_odd_palindrome(100) == (18, 40)
