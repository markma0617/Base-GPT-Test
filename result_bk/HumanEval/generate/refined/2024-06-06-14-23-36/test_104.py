from code_104 import unique_digits

def test():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([987, 13579, 333, 1111]) == [333, 987, 1111]
