from code_160 import do_algebra

def test():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '-', '+'], [10, 5, 2, 3]) == 11
    assert do_algebra(['+', '*', '//', '**'], [100, 5, 2, 6]) == 75
    assert do_algebra(['**', '-', '*'], [2, 3, 4, 2]) == -30
    assert do_algebra(['//', '+'], [15, 3, 2]) == 7
    assert do_algebra(['*'], [4, 5]) == 20
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [5, 3]) == 2
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['//'], [10, 4]) == 2
