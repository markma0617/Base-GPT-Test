from code_29 import filter_by_prefix
def test():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['python', 'java', 'ruby', 'scala'], 'j') == ['java']
    assert filter_by_prefix(['apple', 'banana', 'orange', 'grape'], 'b') == ['banana']
    assert filter_by_prefix(['cat', 'dog', 'elephant', 'turtle'], 'e') == ['elephant']