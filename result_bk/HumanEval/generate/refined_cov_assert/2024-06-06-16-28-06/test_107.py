from code_107 import even_odd_palindrome

def test():
    assert even_odd_palindrome(0) == (0, 0)
    assert even_odd_palindrome(1) == (0, 1)
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(5) == (1, 3)
    assert even_odd_palindrome(9) == (2, 5)
    assert even_odd_palindrome(10) == (2, 5)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(15) == (6, 8)
    assert even_odd_palindrome(20) == (7, 12)
    assert even_odd_palindrome(100) == (41, 60)
