from code_21 import rescale_to_unit
def test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1.0, 5.0, 7.0, 3.0, 2.0]) == [0.0, 1.0, 1.4, 0.4, 0.2]
    assert rescale_to_unit([10.0, 20.0, 15.0, 25.0, 5.0]) == [0.0, 0.5, 0.25, 0.75, 0.0]