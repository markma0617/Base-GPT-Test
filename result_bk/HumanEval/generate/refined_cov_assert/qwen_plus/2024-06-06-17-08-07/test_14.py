from code_14 import all_prefixes

def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
    assert all_prefixes('python') == ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']
    assert all_prefixes('') == []
    assert all_prefixes('12345') == ['1', '12', '123', '1234', '12345']
    assert all_prefixes('abcdefg') == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
    assert all_prefixes('test_case') == ['t', 'te', 'tes', 'test', 'test_', 'test_c', 'test_ca', 'test_cas', 'test_case']
    assert all_prefixes('longest_string') == ['l', 'lo', 'lon', 'long', 'longe', 'longes', 'longest', 'longestr', 'longestri', 'longestrin', 'longest_str', 'longest_stri', 'longest_strin', 'longest_string']
    assert all_prefixes('short') == ['s', 'sh', 'sho', 'shot']
    assert all_prefixes('one_word') == ['o', 'on', 'one', 'one_']
