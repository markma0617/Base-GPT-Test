from code_65 import circular_shift
def test_circular_shift():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(1234, 1) == "4123"
    assert circular_shift(1234, 2) == "3412"
    assert circular_shift(1234, 3) == "2341"
    assert circular_shift(1234, 4) == "1234"
    assert circular_shift(1234, 5) == "4321"
    assert circular_shift(1234, 6) == "3412"
    assert circular_shift(1234, 7) == "2341"
    assert circular_shift(1234, 8) == "1234"
    assert circular_shift(1234, 9) == "4321"