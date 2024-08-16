from code_104 import unique_digits

def test():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([5, 7, 9]) == [5, 7, 9]
    assert unique_digits([11, 13, 15]) == [11, 13, 15]
    assert unique_digits([123, 321, 543]) == [123, 321, 543]
    assert unique_digits([111, 333, 555]) == [111, 333, 555]
    assert unique_digits([2, 4, 6]) == []
    assert unique_digits([8, 88, 888]) == []
    assert unique_digits([0, 10, 100]) == [0]
    assert unique_digits([135, 579, 143]) == [135, 143]
