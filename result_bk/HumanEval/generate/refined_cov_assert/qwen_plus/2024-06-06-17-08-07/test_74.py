from code_74 import total_match

def test():
    assert total_match([], []) == []
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert total_match(['short', 'longer'], ['shortest', 'medium']) == ['short', 'longer']
    assert total_match(['a', 'bb', 'ccc'], ['aa', 'b']) == ['aa', 'b']
    assert total_match(['one', 'two', 'three'], ['1', '2', '3', '4']) == ['one', 'two', 'three']
    assert total_match(['abc', 'def'], ['abcdef']) == ['abcdef']
    assert total_match(['12', '345'], ['1', '2', '3', '4', '5']) == ['12', '345']
