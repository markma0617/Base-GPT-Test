from code_104 import unique_digits
def test():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([111, 333, 555, 777]) == [111, 333, 555, 777]