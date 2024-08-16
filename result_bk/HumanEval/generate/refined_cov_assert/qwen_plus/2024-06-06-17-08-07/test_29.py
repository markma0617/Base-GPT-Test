from code_29 import filter_by_prefix

def test():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['apple', 'banana', 'apricot', 'grape'], 'a') == ['apple', 'apricot']
    assert filter_by_prefix(['cat', 'dog', 'cow', 'bat'], 'c') == []
    assert filter_by_prefix(['code', 'coding', 'coder', 'coffee'], 'co') == ['code', 'coding', 'coder']
    assert filter_by_prefix(['hello', 'world', 'hi', 'whatsup'], 'h') == ['hello', 'hi']
    assert filter_by_prefix(['python', 'java', 'javascript', 'ruby'], 'j') == ['java', 'javascript']
    assert filter_by_prefix(['moon', 'sun', 'star', 'earth'], 's') == ['sun', 'star']
    assert filter_by_prefix(['test1', 'test2', 'test3', 't4'], 't') == ['test1', 'test2', 'test3', 't4']
    assert filter_by_prefix(['book', 'pen', 'pencil', 'paper'], 'q') == []
