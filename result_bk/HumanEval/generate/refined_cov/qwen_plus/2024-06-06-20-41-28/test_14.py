from code_14 import all_prefixes

def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert all_prefixes('') == []
