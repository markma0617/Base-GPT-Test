from code_10 import is_palindrome
def test():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('racecar') == True

    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'