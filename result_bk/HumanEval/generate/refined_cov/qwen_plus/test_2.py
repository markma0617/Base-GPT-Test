from code_2 import truncate_number
def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.23) == 0.23
    assert truncate_number(9.999) == 0.999
    assert truncate_number(10.0) == 0.0
    assert truncate_number(0.123) == 0.123