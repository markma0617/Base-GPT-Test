from code_27 import flip_case

def test():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flip_case('abc123') == 'ABC123'
    assert flip_case('123') == '123'
    assert flip_case('') == ''
    assert flip_case('aBcDeF') == 'AbCdEf'
    assert flip_case('XYZ') == 'xyz'
    assert flip_case('12ab34CD') == '12AB34cd'
    assert flip_case('!@#') == '!@#'
    assert flip_case('loReM IpSuM') == 'LOrEm iPsUm'
