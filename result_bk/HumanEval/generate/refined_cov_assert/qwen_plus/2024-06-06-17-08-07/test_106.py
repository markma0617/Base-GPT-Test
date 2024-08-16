from code_106 import f

def test():
    assert f(0) == []
    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 3]
    assert f(4) == [1, 2, 6, 4]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(7) == [1, 2, 6, 24, 15, 720, 364]
    assert f(8) == [1, 2, 6, 24, 15, 720, 364, 40320]
    assert f(9) == [1, 2, 6, 24, 15, 720, 364, 40320, 362880]
