from code_65 import circular_shift
def test():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 3) == "34512"
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(12345, 6) == "54321"
    assert circular_shift(12345, 7) == "45123"
    assert circular_shift(54321, 3) == "32154"
    assert circular_shift(54321, 5) == "54321"
    assert circular_shift(54321, 6) == "15432"
    assert circular_shift(54321, 7) == "32154"
    assert circular_shift(54321, 10) == "54321"