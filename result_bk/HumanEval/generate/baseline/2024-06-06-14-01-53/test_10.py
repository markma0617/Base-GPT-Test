from code_10 import make_palindrome
from code_10 import is_palindrome
def test():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'