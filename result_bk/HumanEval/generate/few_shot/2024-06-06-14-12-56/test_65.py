from code_65 import circular_shift

def test():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(12345, 6) == "54321"
