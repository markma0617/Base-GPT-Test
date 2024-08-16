from code_98 import count_upper
def test():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('ABCDEF') == 3
    assert count_upper('aBcDeF') == 2
    assert count_upper('aeiou') == 0
    assert count_upper('UPPERCASE') == 3
    assert count_upper('randomString') == 1
    assert count_upper('123456') == 0
    assert count_upper('AaBbCc') == 2