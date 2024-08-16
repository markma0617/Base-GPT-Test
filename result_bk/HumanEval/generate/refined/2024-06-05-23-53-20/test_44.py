from code_44 import change_base
def test():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 5) == '20'
    assert change_base(15, 8) == '17'
    assert change_base(16, 2) == '10000'