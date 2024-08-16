from code_48 import is_palindrome

def test():
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('abcba') == True
    assert is_palindrome('level') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('racecar') == True
    assert is_palindrome('python') == False
    assert is_palindrome('deified') == True
