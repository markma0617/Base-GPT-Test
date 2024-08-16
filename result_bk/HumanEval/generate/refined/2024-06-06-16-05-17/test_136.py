from code_136 import largest_smallest_integers

def test():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-5, -2, 0, 3, 8, 10]) == (-2, 3)
    assert largest_smallest_integers([-1, -3, -6, -8]) == (-1, None)
