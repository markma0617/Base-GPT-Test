from code_30 import get_positive

def test():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert get_positive([-10, -5, 0]) == []
    assert get_positive([0, 1, 2, 3]) == [1, 2, 3]
    assert get_positive([10, -10, 20, -20]) == [10, 20]
    assert get_positive([4, 5.5, 6.6]) == [4, 5.5, 6.6]
    assert get_positive([1e-9, 0.0, 1e-5]) == [1e-9, 1e-5]
    assert get_positive([1, 2, 3, -4, -5, -6]) == [1, 2, 3]
    assert get_positive([0.1, -0.2, 0.3]) == [0.1, 0.3]
    assert get_positive([-99, 0, 100]) == [100]
