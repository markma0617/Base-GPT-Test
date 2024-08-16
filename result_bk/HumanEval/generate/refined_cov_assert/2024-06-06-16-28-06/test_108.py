from code_108 import count_nums

def test():
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([0, 0, 0]) == 0
    assert count_nums([-1, -2, -3]) == 3
    assert count_nums([123, 456, 789]) == 3
    assert count_nums([10, 20, 30, -40, -50, -60]) == 6
    assert count_nums([-10, -20, -30, 40, 50, 60]) == 6
    assert count_nums([111, -222, 333, -444, 555]) == 5
    assert count_nums([-111, -222, -333, -444, -555]) == 5
