from code_4 import mean_absolute_deviation
def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == 0.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.0
    assert mean_absolute_deviation([10.0, 20.0, 30.0, 40.0, 50.0]) == 20.0
    assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0
    assert mean_absolute_deviation([1.0, 3.0, 5.0, 7.0, 9.0]) == 2.0
    assert mean_absolute_deviation([2.5, 5.0, 7.5, 10.0]) == 2.5
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0
    assert mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]) == 1.0
    assert mean_absolute_deviation([-1.0, 2.0, -3.0, 4.0]) == 2.0