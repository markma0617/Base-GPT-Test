from code_22 import filter_integers
def test():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([]) == []
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert filter_integers([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert filter_integers([1.1, 2.2, 3.3, 4.4, 5.5]) == []
    assert filter_integers(['hello', 'world']) == []
    assert filter_integers([True, False, 1, 0]) == [1, 0]
    assert filter_integers([1.0, 2.0, 3.0, 4.0, 5.0]) == [1, 2, 3, 4, 5]