from code_133 import sum_squares
def test():
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84
    assert sum_squares([1.4, 4.2, 0]) == 29
    assert sum_squares([-2.4, 1, 1]) == 6
    assert sum_squares([0, 0, 0]) == 0
    assert sum_squares([-1, -1, -1]) == 3
    assert sum_squares([1.1, 2.2, 3.3]) == 19
    assert sum_squares([0.9, 2.6, 3.9]) == 18
    assert sum_squares([-1.1, -2.2, -3.3]) == 19