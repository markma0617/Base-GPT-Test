from code_51 import remove_vowels

def test():
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'
    assert remove_vowels('Hello, World!') == 'Hll, Wrld!'
    assert remove_vowels('Python is fun') == 'Pythn s fn'
    assert remove_vowels('aeiouAEIOU') == ''
    assert remove_vowels('A quick brown fox jumps over the lazy dog.') == 'qck brwn fx jmps vr th lzy dg.'
