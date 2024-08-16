from code_22 import filter_integers

def test():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([True, 42, 7.2, 'hello', [], None]) == [42]
    assert filter_integers([-10, 'foo', 3.1415, {}, 99]) == [-10, 99]
    assert filter_integers([[], {}, '', 123, 0, False]) == [123, 0]
    assert filter_integers([None, 1, '2', 3.0, {'key': 'value'}, (4,)]) == [1]
    assert filter_integers([1.234, '456', -7, '89', '10']) == [-7]
    assert filter_integers([{'a': 1}, 2, [3], (4,), {5}]) == [2, 4]
    assert filter_integers([]) == []
    assert filter_integers([None, None, None]) == []
