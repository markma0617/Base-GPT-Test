from code_160 import do_algebra
def test_do_algebra():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['**', '+', '//'], [2, 3, 4, 5, 2]) == 16
    assert do_algebra(['-', '*', '+', '**'], [5, 4, 3, 2, 1]) == 8