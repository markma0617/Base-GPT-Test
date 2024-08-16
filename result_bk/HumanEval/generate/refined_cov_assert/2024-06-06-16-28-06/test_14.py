from code_14 import all_prefixes

def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('') == []
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert all_prefixes('12345') == ['1', '12', '123', '1234', '12345']
    assert all_prefixes('xyz') == ['x', 'xy', 'xyz']
    assert all_prefixes('python') == ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']
    assert all_prefixes('testing') == ['t', 'te', 'tes', 'test', 'testi', 'testin', 'testing']
    assert all_prefixes('unit') == ['u', 'un', 'uni', 'unit']
    assert all_prefixes('code') == ['c', 'co', 'cod', 'code']
    assert all_prefixes('generate') == ['g', 'ge', 'gen', 'gene', 'gener', 'genera', 'generat', 'generate']
