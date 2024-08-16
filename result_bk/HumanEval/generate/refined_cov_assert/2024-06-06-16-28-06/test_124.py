from code_124 import valid_date

def test():
    assert valid_date('03-11-2000') == True
    assert valid_date('15-01-2012') == False
    assert valid_date('04-0-2040') == False
    assert valid_date('06-04-2020') == True
    assert valid_date('06/04/2020') == False
    assert valid_date('2-29-2020') == True
    assert valid_date('2-30-2020') == False
    assert valid_date('13-11-2000') == False
    assert valid_date('03-00-2000') == False
    assert valid_date('03-11-20000') == False
