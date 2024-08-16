from code_160 import do_algebra

def test():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '*', '//'], [2, 3, 4, 5]) == 2
    assert do_algebra(['-', '+', '*'], [10, 5, 2, 3]) == 17
    assert do_algebra(['//', '**'], [10, 2, 3]) == 9
    assert do_algebra(['*', '-', '+', '//'], [2, 3, 4, 5, 2]) == 5
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['*', '+'], [2, 3, 4]) == 14
    assert do_algebra(['*', '**', '-'], [2, 3, 4, 2]) == 22
