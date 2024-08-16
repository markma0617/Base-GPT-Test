from code_104 import unique_digits

def test():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([9, 11, 21, 35, 53, 91]) == [9, 11, 35, 53]
    assert unique_digits([12, 345, 67, 89, 23]) == [67, 89]
    assert unique_digits([111, 222, 333, 444]) == [111]
