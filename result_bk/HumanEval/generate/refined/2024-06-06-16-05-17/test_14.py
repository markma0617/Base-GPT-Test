from code_14 import all_prefixes

def test():   
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('') == []
    assert all_prefixes('python') == ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']