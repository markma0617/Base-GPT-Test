from code_108 import count_nums

def test():
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([-9, 10, 123, -123]) == 3
    assert count_nums([0, -0, -12, 111]) == 2
