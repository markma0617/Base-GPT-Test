from code_2 import truncate_number

def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(9.99) == 0.99
