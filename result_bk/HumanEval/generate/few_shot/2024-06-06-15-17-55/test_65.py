from code_65 import circular_shift

def test():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 5) == "54321"
    assert circular_shift(12345, 6) == "54321"
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(12345, 10) == "54321"
