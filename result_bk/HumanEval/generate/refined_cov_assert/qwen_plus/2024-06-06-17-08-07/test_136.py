from code_136 import largest_smallest_integers

def test():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-10, -5, -3, 1, 2, 3]) == (-10, 1)
    assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1)
    assert largest_smallest_integers([-5, -3, -1, 0, 1, 3]) == (-5, 1)
    assert largest_smallest_integers([-1, 0, 1, 2, 3]) == (-1, 1)
    assert largest_smallest_integers([-100, 10, 20, 30]) == (-100, 10)
    assert largest_smallest_integers([1, 3, 5, 7, -9]) == (-9, 1)
    assert largest_smallest_integers([-5, -2, 0, 5, 7]) == (-5, 5)
