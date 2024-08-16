from code_44 import change_base

def test():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 4) == '22'
    assert change_base(15, 5) == '30'
    assert change_base(20, 6) == '122'
