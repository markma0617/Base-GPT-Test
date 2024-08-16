from code_107 import even_odd_palindrome

def test():
    assert even_odd_palindrome(1) == (0, 1)
    assert even_odd_palindrome(2) == (0, 2)
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(5) == (1, 4)
    assert even_odd_palindrome(12) == (4, 6)
