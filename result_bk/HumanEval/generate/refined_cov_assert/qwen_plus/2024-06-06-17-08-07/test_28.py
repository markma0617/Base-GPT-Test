from code_28 import concatenate

def test():
    assert concatenate([]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([' ', 'Hello', ', ', 'World']) == ' Hello, World'
    assert concatenate(['1', '2', '3', '4', '5']) == '12345'
    assert concatenate(['Python', ' ', 'is', ' ', 'fun']) == 'Python is fun'
    assert concatenate(['a', 'a', 'a', 'a']) == 'aaaa'
    assert concatenate(['1', '', '3']) == '13'
    assert concatenate(['   ', 'test', '   ']) == '   test   '
    assert concatenate(['abcdefg', 'hijklmn']) == 'abcdefghilmn'
    assert concatenate(['a' * 100, 'b' * 100, 'c' * 100]) == ('a' * 100 + 'b' * 100 + 'c' * 100)
