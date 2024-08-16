from code_142 import sum_squares

def test():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 70
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 12
    assert sum_squares([-3, 0, 3, 6, -4, 8]) == -204
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 256
    assert sum_squares([9, 10, 11, 12, 13, 14, 15]) == 392
    assert sum_squares([-2, -4, -6, -8]) == -112
    assert sum_squares([5, 10, 15, 20, 25, 30]) == 1300
