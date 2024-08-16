from code_11 import string_xor

def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('101', '011') == '110'
    assert string_xor('111', '111') == '000'
    assert string_xor('000', '111') == '111'
    assert string_xor('100101', '011011') == '111110'
    assert string_xor('001100', '110011') == '111111'
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'
    assert string_xor('', '') == ''
    assert string_xor('1', '') == '1'
