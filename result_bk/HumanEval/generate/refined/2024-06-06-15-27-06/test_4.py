from code_4 import mean_absolute_deviation
def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([1.0, 2.0, 5.0, 4.0]) == 1.0
    assert mean_absolute_deviation([7.5, 8.0, 8.5, 9.0]) == 0.75