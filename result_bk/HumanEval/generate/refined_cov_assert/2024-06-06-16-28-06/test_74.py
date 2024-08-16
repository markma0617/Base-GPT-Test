from code_74 import total_match

def test():
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert total_match(['hi'], ['hi']) == ['hi']
    assert total_match(['a', 'b', 'c'], ['x', 'y']) == ['x', 'y']
    assert total_match([], ['hello']) == ['hello']
    assert total_match(['hello', 'world'], ['python', 'rocks']) == ['hello', 'world']
    assert total_match(['python', 'java', 'c++'], ['ruby', 'perl', 'php']) == ['ruby', 'perl', 'php']
