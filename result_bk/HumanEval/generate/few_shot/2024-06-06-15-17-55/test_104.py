from code_104 import unique_digits

def test():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([246, 351, 193, 980]) == [193, 351]
    assert unique_digits([123, 456, 789, 246, 135]) == [123, 135, 789]
    assert unique_digits([111, 333, 555, 777, 999, 246]) == [111, 333, 555, 777, 999]
