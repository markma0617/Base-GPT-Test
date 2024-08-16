from code_107 import even_odd_palindrome

def test():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(100) == (45, 54)
    assert even_odd_palindrome(101) == (45, 55)
    assert even_odd_palindrome(111) == (46, 65)
    assert even_odd_palindrome(999) == (495, 499)
    assert even_odd_palindrome(1000) == (495, 499)
    assert even_odd_palindrome(500) == (249, 250)
    assert even_odd_palindrome(1) == (0, 1)
    assert even_odd_palindrome(2) == (1, 1)
