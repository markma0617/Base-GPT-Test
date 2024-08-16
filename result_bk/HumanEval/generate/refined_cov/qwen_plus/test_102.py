from code_102 import choose_num

def test():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 11) == 10
    assert choose_num(25, 26) == 26
    assert choose_num(1, 1) == -1
