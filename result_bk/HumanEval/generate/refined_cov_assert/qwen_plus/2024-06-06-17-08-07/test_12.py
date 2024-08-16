from code_12 import longest

def test():
    assert longest([]) is None
    assert longest(['a']) == 'a'
    assert longest(['a', 'b', 'c']) == 'c'
    assert longest(['abc', 'def', 'ghi']) == 'ghi'
    assert longest(['abc', 'def', 'ghij']) == 'ghij'
    assert longest(['abc', 'defg', 'hijkl']) == 'defg'
    assert longest(['a', 'ab', 'abc', 'abcd']) == 'abcd'
    assert longest(['aa', 'aaa', 'aaaa']) == 'aaaa'
    assert longest(['a' * 100, 'b' * 99]) == 'a' * 100
    assert longest(['a' * 100, 'b' * 100, 'c' * 99]) == 'a' * 100
