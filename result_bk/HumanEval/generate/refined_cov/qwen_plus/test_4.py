from code_4 import mean_absolute_deviation

def test():
    assert round(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 6) == 1.0
    assert round(mean_absolute_deviation([-1.0, 0.0, 1.0, 2.0]), 6) == 0.5
    assert round(mean_absolute_deviation([4.0, 4.0, 4.0, 4.0, 4.0]), 6) == 0.0
