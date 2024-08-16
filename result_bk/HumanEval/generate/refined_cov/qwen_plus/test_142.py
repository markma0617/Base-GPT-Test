from code_142 import sum_squares

def test():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 70
    assert sum_squares([-3, 0, 3, 6, -9]) == -108
