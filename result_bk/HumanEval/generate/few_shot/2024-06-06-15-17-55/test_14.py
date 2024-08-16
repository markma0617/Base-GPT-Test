from code_14 import all_prefixes

def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert all_prefixes('python') == ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']
    assert all_prefixes('testing') == ['t', 'te', 'tes', 'test', 'testi', 'testin', 'testing']
    assert all_prefixes('unit') == ['u', 'un', 'uni', 'unit']
