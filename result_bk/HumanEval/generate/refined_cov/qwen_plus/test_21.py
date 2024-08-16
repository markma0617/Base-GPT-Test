from code_21 import rescale_to_unit

def test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([-10.0, -5.0, 0.0, 5.0, 10.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([100.0, 200.0, 300.0, 400.0, 500.0]) == [0.0, 0.2, 0.4, 0.6, 0.8]