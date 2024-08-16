from code_65 import circular_shift

def test():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(1234, 1) == "3412"
    assert circular_shift(1234, 2) == "4123"
    assert circular_shift(1234, 3) == "1234"
    assert circular_shift(1234, 4) == "4321"
    assert circular_shift(12345, 1) == "34512"
    assert circular_shift(12345, 6) == "51234"
    assert circular_shift(12345, 7) == "45123"
    assert circular_shift(123456, 5) == "654321"
