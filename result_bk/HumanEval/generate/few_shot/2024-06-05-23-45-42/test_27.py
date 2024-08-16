from code_27 import flip_case

def test():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('WORLD') == 'world'
    assert flip_case('Python3.9') == 'pYTHON3.9'
    assert flip_case('abcXYZ') == 'ABCxyz'
    assert flip_case('') == ''
