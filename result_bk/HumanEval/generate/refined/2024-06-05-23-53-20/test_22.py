from code_22 import filter_integers
def test():   
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([1.0, 'string', 3, 4.5, -2, 0]) == [1, 3, -2, 0]