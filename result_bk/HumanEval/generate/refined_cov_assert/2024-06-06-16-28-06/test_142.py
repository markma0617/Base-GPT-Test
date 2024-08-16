from code_142 import sum_squares

def test():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 68
    assert sum_squares([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 162
    assert sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 125
    assert sum_squares([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 27250
    assert sum_squares([-2, -3, -4, -5, -6, -7, -8, -9, -10]) == -105
    assert sum_squares([100, 200, 300, 400, 500]) == 720500
    assert sum_squares([-100, -200, -300, -400, -500]) == -720500
