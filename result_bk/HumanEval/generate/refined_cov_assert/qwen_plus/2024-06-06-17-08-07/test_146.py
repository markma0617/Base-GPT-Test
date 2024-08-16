from code_146 import specialFilter

def test():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([111, 22, 35, 47, 59, 61]) == 2
    assert specialFilter([99, -11, 20, 32, 44, 56]) == 1
    assert specialFilter([-91, 17, 23, 39, 45, 51]) == 2
    assert specialFilter([10, 20, 30, 40, 50, 60]) == 0
    assert specialFilter([135, -77, 19, -31, 43, 55]) == 2
    assert specialFilter([11, 22, 33, 44, 55, 66]) == 0
    assert specialFilter([-75, 111, 33, -55, 77, 99]) == 3
    assert specialFilter([102, 305, -407, 509, -601]) == 2
