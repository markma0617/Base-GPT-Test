from code_11 import string_xor

def test():
    assert string_xor('010', '110') == '100'
    assert string_xor('1010101', '1100110') == '0110011'
    assert string_xor('11111', '00000') == '11111'
    assert string_xor('00000', '11111') == '11111'
