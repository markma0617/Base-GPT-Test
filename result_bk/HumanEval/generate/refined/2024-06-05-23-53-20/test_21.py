from code_21 import rescale_to_unit
def test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([5.0, 3.0, 8.0, 2.0, 10.0]) == [0.4, 0.2, 0.6, 0.0, 1.0]