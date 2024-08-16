from code_124 import valid_date

def test():
    assert valid_date('03-11-2000') == True
    assert valid_date('15-01-2012') == False
    assert valid_date('04-0-2040') == False
    assert valid_date('06-04-2020') == True
    assert valid_date('06/04/2020') == False
    assert valid_date('02-29-2020') == True
    assert valid_date('02-29-2019') == False
    assert valid_date('01-32-2001') == False
    assert valid_date('13-12-2012') == False
    assert valid_date('01-01-0000') == False
