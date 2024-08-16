from code_98 import count_upper

def test():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('ABCD') == 1
    assert count_upper('AEIOU') == 2
    assert count_upper('BDFHJL') == 0
    assert count_upper('aBCDEfG') == 2
    assert count_upper('a') == 0
    assert count_upper('A') == 1
    assert count_upper('AEAEAE') == 3
