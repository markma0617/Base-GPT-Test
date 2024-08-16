from code_146 import specialFilter
def test():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([123, 456, 789, 111]) == 3