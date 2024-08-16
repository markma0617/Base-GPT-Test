from code_2 import truncate_number
def test():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(6.9) == 0.9
    assert truncate_number(10.1) == 0.1