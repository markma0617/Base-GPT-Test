from code_82 import prime_length

def test():
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False
    assert prime_length('') == False
    assert prime_length('a') == False
    assert prime_length('ab') == True
    assert prime_length('abab') == False
    assert prime_length('abcdef') == False
    assert prime_length('prime') == True
