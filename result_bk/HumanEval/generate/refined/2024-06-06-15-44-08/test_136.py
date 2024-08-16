from code_136 import largest_smallest_integers
def test():   
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, 4, 5, -7]) == (-1, 4)
    assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)