from code_4 import mean_absolute_deviation
def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == 0.0
    assert mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]) == 15.0