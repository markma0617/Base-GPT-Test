from code_12 import longest
def test():   
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'