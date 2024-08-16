from code_160 import do_algebra

def test():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-', '*'], [5, 3, 2, 4]) == 3
    assert do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 5
    assert do_algebra(['//', '**'], [10, 2, 3]) == 5
