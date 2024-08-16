from code_98 import count_upper

def test():   
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
