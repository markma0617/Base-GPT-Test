from code_124 import valid_date

def test():
    assert valid_date('03-11-2000') == True
    assert valid_date('15-01-2012') == False
    assert valid_date('04-0-2040') == False
