from code_146 import specialFilter
def test():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([12, 23, 34, 45, 56, 67, 78, 89, 98, 109]) == 3
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
    assert specialFilter([12, 33, 45, 67, 89, 101, 111, 343]) == 4
    assert specialFilter([9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 0
    assert specialFilter([101, 233, 345, 567, 789, 912, 111, 343]) == 2
    assert specialFilter([123, 234, 345, 456, 567, 678, 789, 890, 901]) == 0
    assert specialFilter([15, 33, 54, 76, 95, 1001, 1121, 3943]) == 3
    assert specialFilter([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0