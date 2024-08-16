from code_10 import make_palindrome
from code_10 import is_palindrome

def test():
    assert is_palindrome('racecar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('12321') == True

    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
