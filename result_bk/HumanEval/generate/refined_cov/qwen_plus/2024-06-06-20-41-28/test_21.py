from code_21 import rescale_to_unit

def test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([-10.0, 0.0, 10.0]) == [-1.0, 0.0, 1.0]
    assert rescale_to_unit([42.0, 66.6, 99.9]) == [0.0, 0.2876712328767123, 1.0]
