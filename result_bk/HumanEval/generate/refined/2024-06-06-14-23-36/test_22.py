from code_22 import filter_integers
def test():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers(['test', 3.5, 8, 'hello', 10]) == [8, 10]