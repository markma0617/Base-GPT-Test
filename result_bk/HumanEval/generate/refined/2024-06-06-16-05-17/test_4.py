from code_4 import mean_absolute_deviation

def test():   
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([2.5, 3.5, 4.5, 5.5, 6.5]) == 1.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.2
