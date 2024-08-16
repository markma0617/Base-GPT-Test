from code_2 import truncate_number
def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(10.75) == 0.75
    assert truncate_number(7.0) == 0.0
    assert truncate_number(0.123) == 0.123
    assert truncate_number(5.555) == 0.555