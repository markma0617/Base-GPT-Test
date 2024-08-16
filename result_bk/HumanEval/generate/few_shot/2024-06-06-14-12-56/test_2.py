from code_2 import truncate_number
def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(5.25) == 0.25
    assert truncate_number(7.0) == 0.0