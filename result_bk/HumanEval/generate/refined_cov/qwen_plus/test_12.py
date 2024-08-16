from code_12 import longest

def test():
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'c'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['aa', 'bb', 'cc']) == 'bb'
