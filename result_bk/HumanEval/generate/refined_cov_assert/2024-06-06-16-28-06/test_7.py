from code_7 import filter_by_substring

def test():
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b') == ['abc', 'bacd', 'array']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'c') == ['abc', 'cde', 'array']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'd') == ['bacd', 'cde', 'array']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'e') == ['cde', 'array']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'f') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ab') == ['abc']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'cd') == ['cde']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ar') == ['array']
