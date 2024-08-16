from code_12 import longest

def test():
    assert longest([]) == None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['abc', 'def', 'ghi']) == 'abc'
    assert longest(['apple', 'banana', 'cherry']) == 'banana'
    assert longest(['python', 'java', 'javascript']) == 'javascript'
    assert longest(['car', 'truck', 'motorcycle']) == 'motorcycle'
    assert longest(['cat', 'dog', 'elephant']) == 'elephant'
    assert longest(['fish', 'shark', 'whale']) == 'shark'
    assert longest(['red', 'green', 'blue']) == 'green'
