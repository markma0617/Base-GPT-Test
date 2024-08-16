from code_65 import circular_shift
def test():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(12345, 3) == "34512"
    assert circular_shift(987654, 5) == "987654"
    assert circular_shift(1234, 6) == "4321"