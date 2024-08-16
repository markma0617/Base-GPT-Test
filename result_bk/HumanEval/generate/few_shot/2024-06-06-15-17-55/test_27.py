from code_27 import flip_case
def test():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flip_case('12345') == '12345'
    assert flip_case('HeLLo123') == 'hEllO123'