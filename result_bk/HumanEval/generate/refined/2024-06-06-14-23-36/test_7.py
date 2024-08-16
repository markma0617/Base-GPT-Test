from code_7 import filter_by_substring

def test():
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b') == ['abc', 'bacd']
