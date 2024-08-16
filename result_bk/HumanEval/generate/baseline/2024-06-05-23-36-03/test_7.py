from code_7 import filter_by_substring
def test_filter_by_substring():
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring(['hello', 'world', 'python'], 'w') == ['world']
    assert filter_by_substring(['apple', 'banana', 'cherry'], 'e') == ['apple', 'cherry']
    assert filter_by_substring(['alpha', 'beta', 'gamma'], 'z') == []