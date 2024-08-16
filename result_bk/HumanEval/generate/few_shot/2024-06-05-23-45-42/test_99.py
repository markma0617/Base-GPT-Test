from code_99 import closest_integer

def test():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("-15.3") == -15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("0") == 0
    assert closest_integer("0.5") == 1
