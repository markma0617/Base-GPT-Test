from code_102 import choose_num

def test():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 10) == -1
    assert choose_num(5, 8) == 8
    assert choose_num(2, 4) == 4
    assert choose_num(4, 4) == -1
    assert choose_num(7, 7) == -1
    assert choose_num(2, 3) == -1
    assert choose_num(1, 4) == 4
    assert choose_num(4, 6) == 6
