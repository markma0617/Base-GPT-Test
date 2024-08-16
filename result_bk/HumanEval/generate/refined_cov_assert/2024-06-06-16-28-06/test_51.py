from code_51 import remove_vowels
def test():
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'
    assert remove_vowels('AEIOUaeiou') == ''
    assert remove_vowels('qwertyuiopasdfghjklzxcvbnm') == 'qwrtypsdfghjklzxcvbnm'
    assert remove_vowels('Python is awesome') == 'Pythn s wsm'
    assert remove_vowels('HELLO World') == 'HLL Wrld'