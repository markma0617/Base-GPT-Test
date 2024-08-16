from code_102 import choose_num

def test():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(3, 7) == 6
    assert choose_num(8, 8) == -1
    assert choose_num(10, 13) == 12
