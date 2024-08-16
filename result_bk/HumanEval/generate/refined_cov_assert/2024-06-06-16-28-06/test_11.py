from code_11 import string_xor
def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '000') == '111'
    assert string_xor('1010', '1010') == '0000'
    assert string_xor('111111', '000000') == '111111'
    assert string_xor('000', '111') == '111'
    assert string_xor('1001', '0101') == '1100'
    assert string_xor('1101', '0101') == '1000'
    assert string_xor('01010101', '10101010') == '11111111'
    assert string_xor('111000111', '000111000') == '111111111'
    assert string_xor('010101010', '101010101') == '111111111'