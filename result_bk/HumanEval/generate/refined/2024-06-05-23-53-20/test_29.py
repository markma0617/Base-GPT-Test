from code_29 import filter_by_prefix
def test():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['python', 'java', 'javascript', 'ruby'], 'j') == ['java', 'javascript']
    assert filter_by_prefix(['apple', 'banana', 'cherry', 'pear'], 'b') == ['banana']