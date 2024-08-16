from code_146 import specialFilter

def test():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([10, 11, 12, 13, 14, 15]) == 3
    assert specialFilter([99, 999, 1005, 1019, 22]) == 3
    assert specialFilter([72, 15, 37, 100]) == 1
