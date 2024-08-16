from code_160 import do_algebra

def test():   
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '*', '-'], [5, 2, 1, 10]) == 16
    assert do_algebra(['-', '/', '+'], [10, 5, 3, 2]) == 4
