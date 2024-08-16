from code_136 import largest_smallest_integers

def test():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-2, 0, 1, -3, 5, 7]) == (-2, 1)
    assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-7, None)
    assert largest_smallest_integers([2, 4, 1, 3, -5, -7]) == (None, 1)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3]) == (-3, None)
    assert largest_smallest_integers([1, 1, 1, 1]) == (None, 1)
    assert largest_smallest_integers([2, -4, 1, 3, -5, 7]) == (-5, 1)
