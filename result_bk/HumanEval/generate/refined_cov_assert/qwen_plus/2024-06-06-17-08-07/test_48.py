from code_48 import is_palindrome

def test():
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('racecar') == True
    assert is_palindrome('python') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal, Panama!') == True