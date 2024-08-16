from code_2 import truncate_number

def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(4.71) == 0.71
    assert truncate_number(0.23) == 0.23
    assert truncate_number(123.456) == 0.456
    assert truncate_number(7.0) == 0.0
    assert truncate_number(99.999) == 0.999
    assert truncate_number(1.123456789) == 0.123456789
    assert truncate_number(100.0) == 0.0
    assert truncate_number(0.0001) == 0.0001
    assert truncate_number(123456789.123456789) == 0.123456789
