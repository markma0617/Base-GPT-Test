from code_54 import same_chars

def test():
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabce') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert same_chars('abcdefg', 'ghijklmno') == False
    assert same_chars('hello', 'olleh') == True
    assert same_chars('python', 'typhon') == True
    assert same_chars('aabbcc', 'aabbccdd') == False
