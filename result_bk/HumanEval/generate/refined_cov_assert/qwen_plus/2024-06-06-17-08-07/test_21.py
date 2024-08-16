from code_21 import rescale_to_unit

def test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([-10.0, 0.0, 10.0]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([4.0, 4.0, 4.0]) == [0.0, 0.0, 0.0]
    assert rescale_to_unit([0.0, 0.0, 0.0]) == [0.0, 0.0, 0.0]
    assert rescale_to_unit([100.0, -100.0]) == [1.0, 0.0]
    assert rescale_to_unit([2.0, 1.5, 1.25]) == [0.0, 0.25, 0.5]
    assert rescale_to_unit([0.1, 0.01, 0.001]) == [0.0, 0.1, 0.2]
    assert rescale_to_unit([1e-6, 1e-5, 1e-4]) == [0.0, 0.1, 0.2]
    assert rescale_to_unit([1.0, 1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0, 0.0]
    assert rescale_to_unit([-1.0, -1.0, -1.0, -1.0]) == [0.0, 0.0, 0.0, 0.0]
