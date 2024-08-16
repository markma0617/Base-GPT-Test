from code_104 import unique_digits

def test():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([11, 25, 37, 46]) == [11, 25, 37]
    assert unique_digits([9, 19, 29, 39]) == [9, 19, 29]
    assert unique_digits([53, 71, 97, 101]) == [53, 71, 97, 101]
    assert unique_digits([123, 456, 789]) == []
    assert unique_digits([103, 205, 301]) == [103, 301]
    assert unique_digits([111, 222, 333]) == [111, 222, 333]
    assert unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert unique_digits([999, 111, 33]) == [111, 33, 999]
