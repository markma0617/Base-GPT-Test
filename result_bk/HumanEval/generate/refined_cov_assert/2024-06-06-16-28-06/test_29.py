from code_29 import filter_by_prefix

def test():   
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'e') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'array') == ['array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'arr') == ['array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'abcd') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'bc') == ['bcd']
