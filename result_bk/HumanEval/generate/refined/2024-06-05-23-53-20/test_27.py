from code_27 import flip_case
def test():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('Python') == 'pYTHON'
    assert flip_case('123abcDEF') == '123ABCdef'