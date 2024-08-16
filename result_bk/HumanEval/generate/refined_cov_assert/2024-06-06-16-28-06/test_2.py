from code_2 import truncate_number

def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(0.1234) == 0.1234
    assert truncate_number(10.75) == 0.75
    assert truncate_number(5.999) == 0.999
    assert truncate_number(8.25) == 0.25
    assert truncate_number(1.23456789) == 0.23456789
    assert truncate_number(9.0) == 0.0
    assert truncate_number(4.99) == 0.99
    assert truncate_number(6.666) == 0.666
