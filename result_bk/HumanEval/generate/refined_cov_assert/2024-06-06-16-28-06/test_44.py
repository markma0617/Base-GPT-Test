from code_44 import change_base
def test():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 5) == '20'
    assert change_base(15, 4) == '33'
    assert change_base(20, 6) == '32'
    assert change_base(25, 8) == '31'
    assert change_base(30, 9) == '33'
    assert change_base(35, 10) == '35'
    assert change_base(40, 2) == '101000'