from code_28 import concatenate
def test():
    assert concatenate([]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['hello', 'world']) == 'helloworld'
    assert concatenate(['Python', 'is', 'awesome']) == 'Pythonisawesome'