from code_4 import mean_absolute_deviation

def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == 0.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.0
    assert mean_absolute_deviation([-1.0, 1.0, 3.0, -3.0]) == 2.0
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0, 0.0]) == 0.0
    assert mean_absolute_deviation([1.2, 3.4, 5.6, 7.8]) == 2.8
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == 1.5
    assert mean_absolute_deviation([1.1, 2.2, 3.3, 4.4, 5.5]) == 1.1
    assert mean_absolute_deviation([10.0, -10.0, 0.0]) == 10.0
    assert mean_absolute_deviation([0.1, 0.2, 0.3, 0.4, 0.5]) == 0.1
