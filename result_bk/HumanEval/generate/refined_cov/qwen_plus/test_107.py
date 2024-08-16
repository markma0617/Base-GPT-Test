from code_107 import even_odd_palindrome

def test():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(100) == (45, 55)
    assert even_odd_palindrome(1001) == (495, 506)
