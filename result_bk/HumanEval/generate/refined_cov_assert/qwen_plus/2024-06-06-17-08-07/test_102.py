from code_102 import choose_num

def test():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(15, 16) == 16
    assert choose_num(1, 1) == -1
    assert choose_num(20, 22) == 22
    assert choose_num(23, 20) == -1
    assert choose_num(0, 4) == 4
    assert choose_num(5, 3) == -1
    assert choose_num(6, 6) == 6
    assert choose_num(10, 9) == -1
