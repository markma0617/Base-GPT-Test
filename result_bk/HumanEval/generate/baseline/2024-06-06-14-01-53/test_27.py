from code_27 import flip_case
def test():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('WORLD') == 'world'
    assert flip_case('123abc') == '123ABC'
    assert flip_case('') == ''
    assert flip_case('aBcDeF') == 'AbCdEf'