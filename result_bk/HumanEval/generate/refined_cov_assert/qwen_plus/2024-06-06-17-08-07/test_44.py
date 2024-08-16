from code_44 import change_base

def test():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 4) == '22'
    assert change_base(9, 5) == '24'
    assert change_base(15, 6) == '33'
    assert change_base(20, 7) == '44'
    assert change_base(16, 8) == '20'
    assert change_base(25, 9) == '32'
    assert change_base(31, 10) == '31'
