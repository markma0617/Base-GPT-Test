from code_146 import specialFilter

def test():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 22, 33, 44, 55, 66]) == 0
    assert specialFilter([-99, 11, 33, -55, 77, -77]) == 3
    assert specialFilter([101, 202, -303, 404, -505, 606]) == 2
