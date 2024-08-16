from code_14 import all_prefixes
def test():
    assert all_prefixes('') == []
    assert all_prefixes('a') == ['a']
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('testing') == ['t', 'te', 'tes', 'test', 'testi', 'testin', 'testing']