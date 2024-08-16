from code_108 import count_nums

def test():
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([-9, 10, 123, -123]) == 3
    assert count_nums([0, 0, 0]) == 0
    assert count_nums([-100, 11, 222, -333]) == 2
    assert count_nums([12, -34, 567]) == 3
    assert count_nums([-12, 34, -567, 89]) == 2
    assert count_nums([9, -99, 18, -108]) == 3
    assert count_nums([-111, 222, 333, 444]) == 1
