from code_2 import truncate_number
def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.8) == 0.8
    assert truncate_number(10.2) == 0.2
    assert truncate_number(0.9) == 0.9