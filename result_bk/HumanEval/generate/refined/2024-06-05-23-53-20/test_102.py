from code_102 import choose_num

def test():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(5, 11) == 10
