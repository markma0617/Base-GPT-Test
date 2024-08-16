from code_7 import filter_by_substring

def test():
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring(['apple', 'banana', 'cherry'], 'an') == ['banana']
    assert filter_by_substring(['cat', 'dog', 'hat', 'god'], 'og') == ['dog']
    assert filter_by_substring(['hello', 'world', 'test'], 'wo') == ['world']
    assert filter_by_substring(['python', 'java', 'javascript', 'ruby'], 'java') == ['java']
    assert filter_by_substring(['code', 'coding', 'coder'], 'cod') == ['code', 'coding', 'coder']
    assert filter_by_substring(['one', 'two', 'three'], 'four') == []
    assert filter_by_substring(['abc123', '123abc', '321abc'], '123') == ['abc123', '123abc']
    assert filter_by_substring(['abcdefg', 'ghijklm'], 'def') == ['abcdefg']
