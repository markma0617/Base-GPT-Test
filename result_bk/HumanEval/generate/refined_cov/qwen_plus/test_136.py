from code_136 import largest_smallest_integers

def test():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-10, -5, 3, 7]) == (-10, 3)
    assert largest_smallest_integers([-5, -3, 0, 5, 9]) == (-5, 5)
    assert largest_smallest_integers([1, 3, 5, 7, 9]) == (None, 1)
